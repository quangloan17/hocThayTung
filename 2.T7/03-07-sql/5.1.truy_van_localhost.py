import MySQLdb

dbServer = '127.0.0.1'
dbUser = 'quangcvn'
dbPass = '270588'
dbName = 'quangcvn'

conn = MySQLdb.connect(dbServer,
        dbUser,dbPass,dbName,charset='utf8')

print('connect success')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

cursor.execute("""CREATE TABLE STUDENT (
        id INT NOT NULL AUTO_INCREMENT,
        name  VARCHAR(50),
        address  VARCHAR(100),
        PRIMARY KEY(id))""")

conn.close()