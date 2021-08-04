from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from decouple import config
from flask_bcrypt import Bcrypt

app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = config('HOST_DB')
app.config['MYSQL_DATABASE_USER'] = config('USER_DB')
app.config['MYSQL_DATABASE_PASSWORD'] = config('PASSWORD_DB')
app.config['MYSQL_DATABASE_DB'] = config('DATABASE')
mysql.init_app(app)


@app.route('/')
def index():
    cur = mysql.get_db().cursor()

    cur.execute('SELECT * FROM numeros')
    numeros = cur.fetchall()

    print(numeros)

    return render_template('index.html', numeros=numeros)


if __name__ == '__main__':
    app.run(debug=True)
