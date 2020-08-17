from math import pow
a=str(input("Nhập chuỗi nhị phân: ")) #Nhập một chuỗi
def Chuyen_Bin_DeC(a): #Gọi hàm với tham số a chờ truyền vào
    Dec=0 #gán biến Dec = 0
    for i in range(0,len(a)): #Tạo vòng lặp để lấy các giá trị bên trong chuỗi a
        Dec+=int(a[i])*pow(2,(len(a)-i-1)) # Biến Dec sẽ cộng dồn với công thức và trả về biến Dec
    return Dec #Trả về gía trị Dec
print(a,"-->",Chuyen_Bin_DeC(a)) #In ra số liệu với biến a nhập vào và chuyển từ nhị phân sang thập phân