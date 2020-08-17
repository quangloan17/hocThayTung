#VD4:
#Đọc vào 1 file văn bản: 'input.txt'
#Xuất N(cho trước) dòng đầu tiên
#ra 1 file văn bản "output.txt"

f = open('input.txt','w',encoding='utf-8')
f.write('line1\nline2\nline4line1\nline2\nline4line1\nline2\nline4line1\nline2\nline4line1\nline2\nline4line1\nline2\nline4')
f.close()

N = 10
f = open('input.txt',encoding='utf-8')
lines = f.readlines()
f.close()
print(lines)

f = open('output.txt','w',encoding='utf-8')
f.writelines(lines[:N]) #Thay thế vòng lặp for bằng writelines
f.close()
