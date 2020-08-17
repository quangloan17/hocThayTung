x = input('nhập vào xâu dạng nhị phân = ')

def changeofNumber(x):
    change = 0
    p = len(x)-1
    for i in range(len(x)):
        change += int(x[i]) * pow(2,p)
        p -= 1
    return change
print('chuyển đổi được',changeofNumber(x))
