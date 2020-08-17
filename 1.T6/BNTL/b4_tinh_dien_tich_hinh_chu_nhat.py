#VD1: Viết hàm tính diện tích HCN

def get_area(width,height):
    return width * height
print(get_area(4,5))

#Tính diện tích và chu vi HCN
def get_area_and_perimeter(width,height):
    area = width * height
    perimeter = 2 * area
    return area, perimeter

s,p = get_area_and_perimeter(4,5)
print('Diện tích = ',s, ', Chu vi = ',p )
