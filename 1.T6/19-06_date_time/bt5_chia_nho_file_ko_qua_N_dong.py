#VD5: 
#Đọc vào file văn bản "input.txt"
#Chia file thành các file nhỏ
#Sao cho mỗi file ko có quá N dòng

f = open('input.txt',encoding='utf-8')
lines = f.readlines()
f.close()


i = 0 #Chỉ số tên file 
n = 0 #Số dòng đã ghi
N = 10 #Số dòng trong file

#2. Đề bài: Chia nhỏ file ra theo 10 dòng một file
while n < len(lines): #n > 21 dòng break 
    part = lines[n:n+N] #lấy giá trị trong list để chia dòng [0:10],[10,20],[20,30]
    #TODO: Write part => file 1
    f = open(f'output_{i}.txt','w',encoding='utf-8')
    f.writelines(part) #Thay thế vòng lặp for bằng writelines
    f.close()

    n += len(part) 
    i += 1 #Tên file tăng lên 1

# #1. Writelines cơ bản để chạy vòng lặp
# f = open('output.txt','w',encoding='utf-8')
# f.writelines(lines[:N]) #Thay thế vòng lặp for bằng writelines
# f.close()