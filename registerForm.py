from flask_wtf import FlaskForm
from wtforms import TextField, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, EqualTo, DataRequired,ValidationError


#def validate_password(form, password):
   

class RegisterForm(FlaskForm):
    
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    dateOfBirth = DateField('Date Of Birth', format='%Y-%m-%d')
    email = StringField('Email')
    # password = PasswordField('Password', validators=[
    #     DataRequired(),
    #     EqualTo('confirmpassword', message='Passwords must match'),
    #     Length(min=6,message='password must be at least 6 characters')
    # ])
    password =PasswordField('Password')
    confirmpassword = PasswordField('Repeat Password')
    submit = SubmitField('Register')


