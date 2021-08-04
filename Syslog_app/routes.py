from random import random
import os
import secrets
from flask import redirect, flash, url_for, render_template
from Syslog_app import app, bcrypt, user_generator, savedb, test
from Syslog_app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from datetime import datetime

def _datos(cur):
    cur.execute(
        'SELECT fecha_adquisicion, numero1, numero2 FROM datos_tiempo_real WHERE id = (SELECT MAX(id) FROM datos_tiempo_real)')
    datos_tiempo_real = cur.fetchall()

    json_data = json.dumps(
        {'fecha': datos_tiempo_real[0][0], 'numero1': datos_tiempo_real[0][1], 'numero2': datos_tiempo_real[0][2]})

    yield f"data:{json_data}\n\n"


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', authenticated = test.is_authenticated())

@app.route("/about")
def about():
	return render_template('about.html', title = 'About', authenticated = test.is_authenticated())

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if test.is_authenticated() == 'True':
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = user_generator.user(form.username.data, hashed_password, form.email.data, "Default")
		savedb.cargarDB(user,'AUTHENTICATION', 'users_data')
		flash(f'Cuenta creada para {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', tittle = 'Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if test.is_authenticated() == 'True':
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = test.data_test_db(form.email.data, 'email')
		if user and bcrypt.check_password_hash(test.data_match_db(form.email.data, 'email', 'password'), form.password.data):
			user_login = user_generator.user_login(form.email.data, True, form.remember.data, datetime.now())
			savedb.cargarDB(user_login,'AUTHENTICATION', 'accounting')
			return redirect(url_for('home'))
		else: 
			flash('login fallido mira pa que que fue', 'danger')
	return render_template('login.html', tittle = 'Login', form=form)

@app.route("/logout")
def logout():
	test.logout()
	return redirect(url_for('home'))

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext;
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)
	return picture_fn

@app.route("/account", methods = ['GET', 'POST'])
def account():
	if test.is_authenticated() == 'False':
		return redirect(url_for('home'))
	form = UpdateAccountForm()
	user_data = test.fetchone(test.data_match_db_last('email','accounting'),'email')
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			test.update_picture(user_data['email'], picture_file)
		test.update(user_data['email'], form.username.data, form.email.data)
		return redirect(url_for('logout'))
	image_file = url_for('static', filename='profile_pics/' + user_data['image_file'])
	return render_template('account.html', tittle = 'Account', account = user_data, authenticated = test.is_authenticated(),
							image_file=image_file, form = form)

