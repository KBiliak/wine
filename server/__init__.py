from flask import Flask
from flask_mysqldb import MySQL
from db.wine_repository import WineRepository

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'wine_db'

mysql = MySQL(app)
wineRepository = WineRepository(mysql)

import server.endpoint.wine_endpoint
