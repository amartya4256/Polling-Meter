from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    aadharid = StringField('Aadhar ID', validators=[DataRequired()])
    otp = PasswordField('OTP', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    login = SubmitField('Sign In')