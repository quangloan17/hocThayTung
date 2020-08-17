A = [1, 3, 4, 5, 7, 8] #i = [6]
print(f'A = {A}')
K=int(input('Nhap so K: '))
S=0

for i in range(len(A)):
    S+=A[i]
    if S > K:
        print(f'- i nho nhat de tong > K = {K}  => i = {i} voi tong S = {S}')
        break
if S < K:
   print('Khong ton tai i de tong > K')
    
