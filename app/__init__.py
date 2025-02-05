from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()

migrate = Migrate()

moment = Moment()

login = LoginManager()
login.login_view = 'auth.login' # this route does not exist yet!!!!

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER_MAIN

    db.init_app(app)
    migrate.init_app(app,db)

    # Register Blueprints
    from app.main import main_blueprint as main
    main.template_folder = Config.TEMPLATE_FOLDER_MAIN
    app.register_blueprint(main)

    from app.auth import auth_blueprint as auth
    auth.template_folder = Config.TEMPLATE_FOLDER_AUTH
    app.register_blueprint(auth)

    # doesnt exist yet but we should consider making
    # from app.errors import error_blueprint as errors
    # errors.template_folder = Config.TEMPLATE_FOLDER_ERRORS
    # app.register_blueprint(errors)
    
    login.init_app(app)
    moment.init_app(app)

    return app
