from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost:5432/taskmanager'

db = SQLAlchemy(app)

task = db.Table('tasks', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def index():
    results = db.session.query(task).all()
    for r in results:
        print(r.name)
    else:
        print('empty table')
        
    return ''