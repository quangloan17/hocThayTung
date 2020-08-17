arr = [1,2,3,5,7,8]
#TODO: in ra cac so bang tong 2 so lien truoc
N=len(arr)

for i in range(2, N):
    #if i < 2: continue
    if arr[i] == arr[i-1]+ arr[i-2]:
        print(f'{arr[i-2]}+{arr[i-1]}={arr[i]}')
    
