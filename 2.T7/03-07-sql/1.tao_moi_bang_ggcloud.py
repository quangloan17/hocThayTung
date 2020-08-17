import MySQLdb

dbServer = '34.87.120.250'
dbUser = 'dichthuat'
dbPass = 'quangloan17'
dbName = 'datapro'

db = MySQLdb.connect(dbServer,
        dbUser,dbPass,dbName,charset='utf8')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

cursor.execute("""CREATE TABLE STUDENT (
        id INT NOT NULL AUTO_INCREMENT,
        name  VARCHAR(50),
        address  VARCHAR(100),
        PRIMARY KEY(id))""")

db.close()

print('sucesss')