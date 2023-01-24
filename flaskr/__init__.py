'''
# TODO #

GETTING AN ERROR

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" 
environment variable, 
and a "wsgi.py" or "app.py" module was not found in the current directory.

NEED TO FIGURE OUT HOW TO SET THE FLASK APP uP 
'''
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    # __name__ is the name of the current Python module.
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder. 
    # The instance folder is located outside the flaskr package 
    # and can hold local data that shouldn’t be committed to version control, 
    # such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)

    # sets default configuration
    app.config.from_mapping(
        # used by flask and extensinos to keep dat safe
        # set to dev to provide convenient value when developing
        # should be set to random value when deploying
        SECRET_KEY='dev',
        # is the path to the SQL database
        DATABASE=os.path.join(app.instace_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)

        # ensrue the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app