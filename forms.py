from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo


class RegistrationForm(Flaskform):
    username = StringField('UserName', validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email', validators = [DataRequired(),Email()])
    Password = PasswordField('Password',validators = [DataRequired()])
    ConfirmPassword =PasswordField('Confirm PAssword',validators = [DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')

class LoginForm(Flaskform):
    email=StringField('Email', validators = [DataRequired(),Email()])
    Password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')