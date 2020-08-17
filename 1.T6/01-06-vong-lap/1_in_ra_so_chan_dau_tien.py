arr = [1,2,3,5,7,8,12,22,34]
#TODO: In ra số chẵn đầu tiên

# for x in arr:
#     if x%2==0:
#         print(x)
#         break

#TODO: In ra số chẵn thứ 2:
i = 0
d = []
for x in range(len(arr)):
    if arr[x] % 2 == 0:
        print(x,arr[x])
        break

for x in arr:
    if x % 2 == 0:
        print('   ',x)
        break

# for x in range(a):
#     if a[x]%2==0:
#         print(a[x])
#         break