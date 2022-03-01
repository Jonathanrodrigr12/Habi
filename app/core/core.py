import mysql.connector


miConexion = mysql.connector.connect(port='3309', host='3.130.126.210', user= 'pruebas', passwd='VGbt3Day5R', db='habi_db')
cur = miConexion.cursor()


def close():
    cur.close()