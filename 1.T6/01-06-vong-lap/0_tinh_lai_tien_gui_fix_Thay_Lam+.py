# M : Số tiền gửi ban đầu
# T: Kỳ hạn(tháng)
# p: Lãi suất quy đổi theo năm(%)
# N: Số kỳ hạn
# Yêu cầu: in ra số tiền sau từng kỳ hạn:


M = int(input('Số tiền ban đầu (tr đồng): '))
p = int(input('Lãi suất quy đổi theo năm(%)): '))
T = int(input('Kỳ hạn gửi(tháng): '))
N = int(input('Số kỳ hạn: '))
m = int(input('Số tiền tiết kiệm mỗi tháng: '))

r = T*p/12/100 #Tỷ lệ lợi nhuận
for i in range(1,N+1):
    #TODO: Update M
    M=M*(1+r) + T*m #Cong thuc thay doi tang theo nam (1+r)
    print(f'Số tiền sau kỳ hạn {i}: {round(M,2)} tr VND')
