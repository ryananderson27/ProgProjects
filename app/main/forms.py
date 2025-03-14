from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, Length
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
import sqlalchemy as sqla

from app import db

class create_project(FlaskForm):
    ...

class update_project(FlaskForm):
    ...
    
=======
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import  Length, DataRequired, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget,CheckboxInput
from wtforms_alchemy import PhoneNumberField
from wtforms.widgets import ListWidget,CheckboxInput
from flask_login import current_user
from datetime import datetime
from wtforms.fields import DateField, DecimalField


from app import db
import sqlalchemy as sqla


class EditFacultyForm(FlaskForm):
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
            
class EditStudentForm(FlaskForm):
    firstname = StringField('First Name', validators= [DataRequired()])
    lastname = StringField('Last Name', validators= [DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    phonenumber = PhoneNumberField('Phone Number', validators=[DataRequired()])
    ID = IntegerField('WPI ID', validators=[DataRequired(), Length(min=9,max=9)])
    gpa = DecimalField('Cumulative GPA', validators= [DataRequired()], places=3, rounding=None)
    grad = DateField('Expected Graduation Date', format='%Y-%m-%d', default=datetime.now())
    password = PasswordField('Password', validators= [DataRequired()])
    password2 = PasswordField('Repeat Password', validators= [DataRequired(), EqualTo('password')])
    research_projects = TextAreaField('Past Research Experience', [Length(min=0, max=300)])
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
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662
