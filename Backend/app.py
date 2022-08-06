import json
import uuid
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from Operator import Operator
from setup import Setup
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost:5432/taskmanager_prod'

db = SQLAlchemy(app)
metadata = db.MetaData()
engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/taskmanager_prod')
Session = sessionmaker(bind = engine)
session = Session()

# Load Db mapping
Base = automap_base()
Base.prepare(db.engine, reflect=True)
c = Base.classes

operator = Operator(db, metadata, engine, session, Base)
operator.initialize()


@app.route('/')
def index():
    Shop = Base.classes.shops
    new_shop = Shop(id=uuid.uuid1().__str__(), balance=1)
    db.session.add(new_shop)
    db.session.commit()

    return ''

@app.route('/setup')
def setup():
    setup = Setup().setup(db, Base)
    return ''


@app.route('/bous/<name>', methods=['GET'])
def bou(name):
    return operator(operator.return_bou(name))

@app.route('/shops', methods=['UPDATE'])
def shop():
    return ''

@app.route('/shops/items', methods=['SET', 'GET', 'UPDATE'])
def items():
    if request.method == 'GET':
        return operator(operator.return_all_items())
    elif request.method == 'SET':
        return operator(operator.add_item())
    else:
        pass
    return ''

@app.route('/calendars/<bou>', methods=['GET'])
def calendars(bou):
    return operator(operator.return_calendar(bou))
    
@app.route('/tasks', methods=['SET', 'GET'])
def tasks():
    if request.method == 'GET':
        return operator(operator.return_task_list())
    elif request.method == 'SET':
        operator(operator.add_task(request.json))
    else:
        pass
    return ''

@app.route('/tasks/<task>', methods=['GET', 'UPDATE'])
def tasks_update(task):
    if request.method == 'GET':
        return operator(operator.return_task(task))
    
@app.route('/bous/<bou>', methods=['GET', 'SET', 'UPDATE'])
def bous():
    if request.method == 'GET':
        pass
    elif request.method == 'SET':
        pass
    else:
        pass
    return ''
    
@app.route('/looking_forwardables/<bou_id>', methods=['SET', 'GET', 'UPDATE'])
def looking_forwardables(bou_id):
    if request.method == 'GET':
        return operator(operator.return_looking_forwardables(bou_id))
    elif request.method == 'SET':
        return operator(operator.add_looking_forwardables(bou_id))
    else:
        pass
    return ''
    
    