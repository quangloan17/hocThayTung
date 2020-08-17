import MySQLdb

dbServer = '34.87.120.250'
dbUser = 'dichthuat'
dbPass = 'quangloan17'
dbName = 'datapro'

conn = MySQLdb.connect(dbServer,
        dbUser,dbPass,dbName,charset='utf8')

student_no = input('Nhập mã SV: ')
#1. Dễ bị hack vì ghép param vào trong lệnh SQL
# sql = f'''SELECT * FROM student
#         WHERE name LIKE '%{keyword}%'
#         OR student_no LIKE '%{keyword}%'
#         '''
#2. Thay thế bằng %s và thêm nhiều %s %s tương ứng param truyền vào
sql = '''SELECT * FROM student
        WHERE student_no = %s
        '''
#hướng dẫn cách Hack: keyword = 1' OR 1=1 OR 1=' để tránh Hack ta sẽ sử dụng template python %s
cursor = conn.cursor()
cursor.execute(sql,[student_no]) #Truyền param vào đây theo cách 2
print(cursor.fetchall())