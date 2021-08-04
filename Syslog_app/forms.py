from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, StringField, SubmitField, PasswordField
from wtforms.validators import ValidationError, Email, Length, DataRequired, EqualTo, ValidationError
from Syslog_app import test

class RegistrationForm(FlaskForm):
    username = StringField('Usuario'
    , validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired()])
    confirm_password =  PasswordField('Confirmar Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = test.data_test_db(username.data, 'username')
        if user:
            raise ValidationError('ya agarraron ese usuario')

    def validate_email(self, email):
        user = test.data_test_db(email.data,'email')
        if user:
            raise ValidationError('ya agarraron ese email')

class UpdateAccountForm(FlaskForm):
    username = StringField('Usuario'
    , validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Actualizar')

    def validate_username(self, username):
        if username.data != test.fetchone(test.data_match_db_last('email','accounting'), 'email')['username']:
            user = test.data_test_db(username.data, 'username')
            if user:
                raise ValidationError('ya agarraron ese usuario')

    def validate_email(self, email):
        if email.data != test.fetchone(test.data_match_db_last('email','accounting'),'email')['email']:
            user = test.data_test_db(email.data,'email')
            if user:
                raise ValidationError('ya agarraron ese email')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

