#VD: Đọc file

# f = open("text.txt")
# text = f.read() #result as string
# f.close()

# print(text)

#VD2: write file:
f = open('output.txt','w',encoding='utf-8')
f.write('Chào các bạn\nTôi đang đi chơi\n Đi chơi vui thật')
f.close()

#VD3: sử dụng with để ko phải đóng file sau khi ht block
#with open('output.txt','w') as f:
#     print(f.read())