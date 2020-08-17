#VD03
#In ra các số xuất hiện nhiều hơn 2 lần có hay không
lst = [23,4,6,7,9,4,78]
    
found = False

N = len(lst)

for i in range(N):
    for j in range(N):
        if lst[i]==lst[j] and i != j:
            found = True
            break
print(found)
