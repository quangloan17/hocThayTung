for a in range(10,100):
    if a % 10 == 0:
        a = a//10+a+1
        if a < 100:
            print(a,',',int(str(a)[::-1]))
