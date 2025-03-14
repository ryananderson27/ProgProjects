from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import sqlalchemy as sqla

from app import db
from app.main.forms import create_project, update_project