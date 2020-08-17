import csv

with open('student.csv',encoding = 'utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    data_rows = list(reader)
header_row.append('Diem TB')

for row in data_rows:
    hs1,hs2,hs3 = int(row[1]),int(row[2]), int(row[3])
    diemtb = round((hs1 + hs2*2 + hs3*3)/6,1)
    row.append(diemtb)

with open('student_bd.csv', 'w',encoding = 'utf-8',newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header_row)
    writer.writerows(data_rows)