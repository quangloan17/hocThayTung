#P: Giá sản phẩm mua
#M: Số tiền trả ban đầu
#m: Số tiền trả mỗi tháng
#r: Lãi suất tháng

P = int(input('Giá sản phẩm mua là: '))
M = int(input('Số tiền trả trước ban đầu: '))

m = int(input('Số tiền trả sau mỗi tháng: '))
r = int(input('Lãi suất tháng(%) : '))

R = P - M #Số tiền còn lại phải trả

#TODO: Tìm  số tháng T để thanh toán hết
T = 0
while R > 0: #R là tiền lãi R<0 thì vòng lặp kết thúc
    T += 1
    #TODO: Update R
    R = (R - m) + (R * r/100) #R-m là số tiền còn lại trừ số tiền trả sau
    print('Tháng ' ,T,'trả lãi va số tiền còn lại: ', R)
