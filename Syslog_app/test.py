from Syslog_app import savedb, user_generator
from datetime import datetime

def data_test_db(data, type_data):
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f'SELECT * FROM users_data where {type_data} = "{data}"')
        return cur.fetchone()

def data_match_db(data, type_data, column, table = 'users_data'):
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f'SELECT {column} FROM {table} where {type_data} = "{data}"')
        return cur.fetchone()[0]

def data_match_db_last(type_data, table = 'users_data'):
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f'SELECT {type_data} FROM {table} ORDER BY id DESC LIMIT 1')
        return cur.fetchone()[0]

def is_authenticated():
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute('SELECT login_state FROM accounting ORDER BY id DESC LIMIT 1')
        return cur.fetchone()[0]

def logout():
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f'SELECT * FROM accounting ORDER BY id DESC LIMIT 1')
        data = cur.fetchone()
        user_login = user_generator.user_login(data[1], False, data[3], datetime.now())
        savedb.cargarDB(user_login,'AUTHENTICATION', 'accounting')

def fetchone(data, data_type):
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f"SELECT username, email, image_file FROM users_data WHERE {data_type} = '{data}'")
        data = cur.fetchone()
        user_data = {'username' : data[0],'email': data[1], 'image_file': data[2]} 
        return user_data;

def update(email, new_username, new_email):
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f"UPDATE users_data SET username = '{new_username}', email = '{new_email}' WHERE email = '{email}'")
        mydb.commit()

def update_picture(email, new_image_file):
        print(new_image_file)
        mydb = savedb.connectarDB('AUTHENTICATION')
        cur = mydb.cursor()
        cur.execute(f"UPDATE users_data SET image_file = '{new_image_file}' WHERE email = '{email}'")
        mydb.commit()




 



