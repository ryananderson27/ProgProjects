from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, IntegerField
from wtforms.validators import  Length, DataRequired, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.widgets import ListWidget,CheckboxInput
from wtforms_alchemy import PhoneNumberField
from flask_login import current_user

from app import db
import sqlalchemy as sqla


class EditForm(FlaskForm):
    firstname = StringField('First Name', validators= [DataRequired()])
    lastname = StringField('Last Name', validators= [DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    phonenumber = PhoneNumberField('Phone Number', validators=[DataRequired()])
    ID = IntegerField('WPI ID', validators=[DataRequired(), Length(min=9,max=9)])
    password = PasswordField('Password', validators= [DataRequired()])
    password2 = PasswordField('Repeat Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Make Changes')
    
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
    
    def validate_username(self, username):
        query = sqla.select(User).where(User.username == username.data)
        user = db.session.scalars(query).first()
        if user is not None:
            raise ValidationError('Username Taken! Please use a different username.')

    def validate_email(self, email):
        query = sqla.select(User).where(User.email == email.data)
        User = db.session.scalars(query).first()
        if User is not None:
            if User.id != current_user.id:
                raise ValidationError('Email Taken! Please use a different email account.')
            
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')