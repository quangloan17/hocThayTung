a = 'tôi đang đi chơi, tôi đang học'
b = a.split()
#print(b,type(b))

c = len(b)
count = 0
for i in range(c):
    for j in range(i+1,c):
        if b[i] == b[j] and i != j:
            count += 1
    print(i,j,b[i],count)