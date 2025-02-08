from flask_wtf import FlaskForm
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
    