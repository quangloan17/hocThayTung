#TODO: Nhap so N
#Tinh tong: 1+2+...+N

N = int(input('Nhập số N: '))

S=0
for i in range(1, N+1):
    S+=i

print(S)
