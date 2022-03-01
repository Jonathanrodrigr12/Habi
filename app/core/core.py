import mysql.connector
from app.constants_file import Constants


miConexion = mysql.connector.connect(port=Constants.PORT, host=Constants.URL,
user= Constants.USER, passwd=Constants.PASSWORD, db=Constants.db)
cur = miConexion.cursor()


def close():
    cur.close()