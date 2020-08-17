# Nhập vào số nhị phân
nhi_phan = input("Nhập vào số nhị phân: ")

def thap_phan(nhi_phan): 
    thap_phan = 0 
    for so in nhi_phan: 
        thap_phan = thap_phan*2 + int(so) 
    print("Số thập phân là: ", thap_phan)


# Gọi hàm
thap_phan(nhi_phan)
