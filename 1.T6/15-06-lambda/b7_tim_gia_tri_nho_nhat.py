#VD4:
#Cho 1 hàm f và 2 điểm a,b
#Todo: Tim vị trí nhỏ nhất của f
#chính xác đến 0.001
def find_min(f,a,b):
    dx = 0.001
    x = a
    xmin = x
    fmin = f(x)
    
    while x <= b:
        x += dx
        fx = f(x)
        if fx < fmin:
            xmin = x
            fmin = fx
        return xmin

print(find_min(lambda x:2*x*x - x + 1, 0,1))
#min phải bằng 0.25