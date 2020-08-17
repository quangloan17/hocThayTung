str1=input("Input string: ")
count=0
for i in range(len(str1)):
    if str1[i]!=" ":
        count+=1
print("Số ký tự có trong string:",count)
