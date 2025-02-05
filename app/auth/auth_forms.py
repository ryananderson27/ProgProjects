from flask_wtf import FlaskForm
from datetime import datetime
from wtforms.fields import DateField, DecimalField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Email, Length
from wtforms_alchemy import PhoneNumberField
from wtforms.widgets import ListWidget,CheckboxInput

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
     Student = SubmitField('Register')

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


class StudentRegistrationForm(FlaskForm):
     #Maybe make since a dropdown?
     gpa = DecimalField('Cumulative GPA', validators= [DataRequired()], places=3, rounding=None)
     grad = DateField('Expected Graduation Date', format='%Y-%m-%d', default=datetime.now())
     #This might need some editing, my idea is that we have all the projects in the data in there own class
     # and we have a object that designates what topic they fall under, like a Soft Eng project would fall under 'CS'
     #Open to changes, and by all means if there is a better way to do this, go ahead.
     topics = QuerySelectMultipleField('Research Topics',
                                       query_factory = lambda : db.session.scalars(sqla.select(Projects.topic).order_by(Project)),
                                       get_label = lambda theTopic : theTopic.name,
                                       widget = ListWidget(prefix_label=False),
                                       option_widget =CheckboxInput())
     code = QuerySelectMultipleField('Research Topics',
                                       query_factory = lambda : db.session.scalars(sqla.select(Projects.code).order_by(Project)),
                                       get_label = lambda theCode : theCode.name,
                                       widget = ListWidget(prefix_label=False),
                                       option_widget =CheckboxInput())
     majors = QuerySelectMultipleField('Majors', 
                query_factory = lambda : db.session.scalars(sqla.select(Major).order_by(Major.name)),
                get_label = lambda theMajor : theMajor.name,
                widget=ListWidget(prefix_label=False),
                option_widget=CheckboxInput())


class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

