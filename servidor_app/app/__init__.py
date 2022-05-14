from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import (connection)
import sqlalchemy

#connection.execute('set max_allowed_packet=67108864') ##uma dica do stack overflow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:33743571@localhost:3306/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #evitar saida do banco de dados
app.config['SECRET_KEY'] = '33743571' #para logar


db = SQLAlchemy(app)
login_manager = LoginManager(app)
engine = sqlalchemy.create_engine('mysql+pymysql://root:33743571@localhost:3306/flask_database')
#'mysql://root:33743571@localhost/mydatabase'

#'mysql://root:senha@localhost/nomedatabase