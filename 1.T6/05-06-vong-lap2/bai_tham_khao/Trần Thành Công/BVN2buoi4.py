str1=input("Nhập xâu: ")
for i in range(len(str1)):
    if str1[i]==".":
        str1[i+1].upper()
if str1[0]!=" ":
    str1[0].upper()
print("Xâu sau khi đc chuẩn hóa: \n",str1)
