#json_parse.py

import json

with open('students.json') as f:
    result = json.load(f) #Cách 1
    #result = json.loads(f.read()) #Cách 2:loads là viết tắt load string
    print(result.__class__) #Hàm class để xem loại đối tượng
    for i,item in enumerate(result):
        print(f'Record {i}:')
        print(f'\tName:{item["name"]},studentNo:f{item["studentNo"]}')
        print(f'\tCourses:{item["courses"]}')
        for course in item['courses']:
            print(f'\t\t{course["name"]}({course["code"]})')