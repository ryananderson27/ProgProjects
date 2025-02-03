from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Email, Length
from wtforms_alchemy import PhoneNumberField

from app import db
import sqlalchemy as sqla

class RegistrationForm(FlaskForm):
     firstname = StringField('First Name', validators= [DataRequired()])
     lastname = StringField('Last Name', validators= [DataRequired()])
     username = StringField('Username', validators= [DataRequired()])
     email = StringField('Email', validators= [DataRequired(), Email()])
     phonenumber = PhoneNumberField('Phone Number', validators=[DataRequired()])
     ID = IntegerField('WPI ID', validators=[DataRequired(), Length(min=9,max=9)])
     password = PasswordField('Password', validators= [DataRequired()])
     password2 = PasswordField('Repeat Password', validators= [DataRequired(), EqualTo('password')])
     submit = SubmitField('Register')

     def validate_username(self, username):
        query = sqla.select(User).where(User.username == username.data)
        user = db.session.scalars(query).first()
        if user is not None:
            raise ValidationError('Username Taken! Please use a different username.') 
     
     def validate_phonenumber(self, phonenumber):
        query = sqla.select(User).where(User.phonenumber == phonenumber.data)
        user = db.session.scalars(query).first()
        if user is not None:
            raise ValidationError('Phone Number in Use!')
        
     def validate_ID(self, ID):
        query = sqla.select(User).where(User.ID == ID.data)
        user = db.session.scalars(query).first()
        if user is not None:
            raise ValidationError('ID is already taken, contact Admin if there is an issue!')
     
     def validate_email(self, email):
        query = sqla.select(User).where(User.email == email.data)
        User = db.session.scalars(query).first()
        if User is not None:
            raise ValidationError('Email Taken! Please use a different email account.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

