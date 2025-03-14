from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()

migrate = Migrate()
<<<<<<< HEAD
login = LoginManager()
login.login_view = 'auth.login'
moment = Moment()

=======

moment = Moment()

login = LoginManager()
login.login_view = 'auth.login' # this route does not exist yet!!!!
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER_MAIN

    db.init_app(app)
    migrate.init_app(app,db)
<<<<<<< HEAD
    login.init_app(app)
    moment.init_app(app) 

    # blueprint registration
=======

    # Register Blueprints
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662
    from app.main import main_blueprint as main
    main.template_folder = Config.TEMPLATE_FOLDER_MAIN
    app.register_blueprint(main)

    from app.auth import auth_blueprint as auth
    auth.template_folder = Config.TEMPLATE_FOLDER_AUTH
    app.register_blueprint(auth)

<<<<<<< HEAD
    from app.errors import error_blueprint as errors
    errors.template_folder = Config.TEMPLATE_FOLDER_ERRORS
    app.register_blueprint(errors)
=======
    # doesnt exist yet but we should consider making
    # from app.errors import error_blueprint as errors
    # errors.template_folder = Config.TEMPLATE_FOLDER_ERRORS
    # app.register_blueprint(errors)
    
    login.init_app(app)
    moment.init_app(app)
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662

    return app
