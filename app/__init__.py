from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CHANGE_THIS'
app.config['SCHEDULER_API_ENABLED'] = True
app.config['SCHEDULER_TIMEZONE'] = 'America/Sao_Paulo'
app.config['SCHEDULER_JOBSTORES'] = {'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite3')}

login_manager = LoginManager(app)
db = SQLAlchemy(app)

scheduler = APScheduler()
scheduler.init_app(app)
