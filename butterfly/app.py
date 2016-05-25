from flask import Flask
from flask_script import Manager as ScriptManager
from flask_seasurf import SeaSurf
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SeaSurf(app)
db = SQLAlchemy(app)

script_manager = ScriptManager(app)


def main():
    script_manager.run()
