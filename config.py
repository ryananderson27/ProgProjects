import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
<<<<<<< HEAD
# load_dotenv(os.path.join(basedir, '.env'))
=======
# load_dotenv(os.path.join(basedir, '.env')) # uncomment this file if we ever need to store any API keys or anything in our .env file!!!
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
<<<<<<< HEAD
        'sqlite:///' + os.path.join(basedir, 'smile.db')
=======
        'sqlite:///' + os.path.join(basedir, 'research.db')
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app//static')
    TEMPLATE_FOLDER_MAIN = os.path.join(basedir, 'app//main//templates')
<<<<<<< HEAD
    TEMPLATE_FOLDER_ERRORS = os.path.join(basedir, 'app//errors//templates')
=======
    # TEMPLATE_FOLDER_ERRORS = os.path.join(basedir, 'app//errors//templates') # This template does not exist atm
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662
    TEMPLATE_FOLDER_AUTH = os.path.join(basedir, 'app//auth//templates')    