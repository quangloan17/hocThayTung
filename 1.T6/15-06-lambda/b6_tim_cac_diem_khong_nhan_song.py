#VD3:
#Cho danh sách điểm phát sóng và thu sóng
#bán kính phủ sóng R
#Tim các điểm ko nhận được sóng

A = [(1,1),(3,3),(4,5),(5,4)] #Phát 
B = [(0.5,0.5),(0.5,1.5),(1.5,2.5),(2.5,2.5),(2.5,4.5)]#Thu 
R = 1


#Step1: Viết hàm khoảng cách/(bình phương khoảng cách)
def distance_square(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return (x1-x2)**2 + (y1-y2)**2


#Step2: Viết hàm kiểm tra 1 điểm thu có nhận được tín hiệu không
def isBlackPoint(p):
    black = True
    for x in A:
        d2 = distance_square(p,x)
        if d2 <= R*R:
            return False
    return True
    
#Step3: In ra các điểm thu không nhận được tín hiệu
for p in B:
    if isBlackPoint(p):
        print(p)
