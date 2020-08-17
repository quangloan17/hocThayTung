arr = [1,2,3,4,12,5,7,13,8]
#TODO
#In ra tất cả các bộ số(a,b,c)
N = len(arr)

for i in range(N):
    a = arr[i]
    for j in range(i+1,N):
        b = arr[j]
        c = a + b
        if c in arr:
            print(f'{a}+{b}={c}')




# # #: a + b = c
# N = len(arr)
# for i in range(N):
#     a = arr[i]
#     for j in range(i+1,N):
#         #TODO: Loại bỏ a==b
#         #if i >= j: continue
#         b = arr[j]
#         c = a + b
#         if c in arr:
#             print(f'{a}+{b}={c}')
