#Nhập vào 2 xâu
#Todo: In ra vị trí đầu tiên 2 xâu khác nhau
#Ví dụ:
#st1 = Hà Nội, st2 = Hà Giang
#---->Vị trí: 3 (N/G)

st1 = input('Xâu 1: ')
st2 = input('Xâu 2: ')

N1 = len(st1)
N2 = len(st2)
N = min(N1,N2)
flag = False

for i in range(N):
    if st1[i]!=st2[i]:
        print(i,st1[i],st2[i])
        flag = True
        break
    
if not flag:
    print('Không tồn tại')
