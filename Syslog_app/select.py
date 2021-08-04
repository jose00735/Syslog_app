import savedb
data = ""
type_data = "username"
mydb = savedb.connectarDB('AUTHENTICATION')
cur = mydb.cursor()
cur.execute(f'SELECT {type_data} FROM users_data where {type_data} = "{data}"')
print(cur.fetchone()[0])