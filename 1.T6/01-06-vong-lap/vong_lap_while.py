#Cho so S:
#Tim so N nho nhat de: 1 + 2 +...+ N > K

K = int(input('K= '))
N = int(input('N= '))

N = 1
S = 0

while S < K:
    S += N
    N += 1
    print(f'S = {S}, N = {N}')
print(f'N nho nhat de tong > K  => N = {N-1}')
