import mysql.connector
from decouple import config
from mysql.connector import connection

def connectarDB(name_db):
    mydb = mysql.connector.connect(
        host='localhost',
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config(name_db)
    )

    return mydb

def guardarDB(mydb, data, table_name):
    cur = mydb.cursor()
    if table_name == 'users_data':
        cur.execute("INSERT INTO {table_name} (username, email, image_file, password) VALUES ('{username}', '{email}', {image_file}, '{password}')"
                    .format(table_name = table_name, username=data['username'], password=data['password'], email=data['email'], image_file=data['image_file']))
    elif table_name == 'accounting':
        cur.execute("INSERT INTO {table_name} (email, login_state, remember, datetime) VALUES ('{email}', '{login_state}', '{remember}', '{datetime}')"
                    .format(table_name = table_name,email=data['email'], login_state=data['login_state'], remember=data['remember'], datetime=data['datetime']))
    mydb.commit()
    

def cargarDB(data,name_db,table_name):
    mydb = connectarDB(name_db)
    guardarDB(mydb,data, table_name)
