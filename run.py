# give terminal and flask shell access to components of app to test them through CLI (without worrying about templates or routes)

# testing thru flask shell with this context processor
    # change value of FLASK_APP in .env from 'app' to 'run.py'(no quotes)


# import the things you need
from app import app
from app.models import db, User

 # shell context processor - gives flask shell (a little terminal that has access to flask app) access to database models, etc.
@app.shell_context_processor
def shell_context():
    return {'db':db, 'User': User}