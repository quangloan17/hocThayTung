studentList = [
{
    'name':'Nguyễn Văn A',
    'studentNo':'10001',
#Khoá học theo dạng list và trong list có các từ điển con
    'courses':[
        {'code':'C001','name':'Python Cơ bản'},
        {'code':'C002','name':'Javascript'}
    ]
},
{
    'name':'Nguyễn Văn B',
    'studentNo':'10002',
#Khoá học theo dạng list và trong list có các từ điển con
    'courses':[
        {'code':'C001','name':'Python Cơ bản'},
        {'code':'C002','name':'Javascript'}
    ]
}
]
import json #Lưu dữ liệu theo dạng NoSQL *** Hay chuyển dữ liệu sang máy khác


#1. indent để sử dụng in ra theo dạng cây,
# json.dump để xuất ra dạng string để gửi online
# json.load để chuyển dữ liệu sang dạng biến của python
# Ví dụ: dict hay list, tuple
print(json.dumps(studentList,indent=2)) 

#2. Sử dụng công thức with open để không phải dùng lệnh f.close
with open('students.json','w') as f:
    json.dump(studentList,f,indent = 2)


#Sử dụng tool https://jsonbeautifier.org để phân tích và làm dự án vì nó bố trí đẹp đẽ