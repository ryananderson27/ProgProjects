import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

from config import Config
from app import create_app, db


app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db}

@app.before_request
def initDB(*args, **kwargs):
    if app.__got_first_request:
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)