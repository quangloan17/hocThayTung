s = input("Xâu : ")

N = len(s) 
n = 0         #so phan tu la chu cai
for i in range(N):
    if s[i].isalpha() :
        n+=1
print(f'so phan tu la chu cai n = {n}')
        