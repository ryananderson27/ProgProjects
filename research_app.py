<<<<<<< HEAD
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

from config import Config
from app import create_app, db

=======
from config import Config
from app import create_app, db
# from app.main.models import User, Student, Faculty # These models dont exist yet
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db}
<<<<<<< HEAD

@app.before_request
def initDB(*args, **kwargs):
    if app.__got_first_request:
        db.create_all()

if __name__ == '__main__':
=======
    # return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'User': User, 'Student': Student, 'Faculty': Faculty} # These models dont exist yet

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

if __name__ == "__main__":
>>>>>>> d0b2bd99ba44dd515a5f6126bfd5bdf5f324b662
    app.run(debug=True)