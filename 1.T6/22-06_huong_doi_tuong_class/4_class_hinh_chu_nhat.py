# VD:
# Viết class Rect:
# 4 trường x1,y1,x2,y2
# 4 method: 
# getArea(), getPerimeter()
# getWidth(),getHeight()
class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def getWidth(self):
        return self.x2 - self.x1
    def getHeight(self):
        return self.y2 - self.y1
    def getArea(self):
        return self.getWidth() * self.getHeight()
    def getPerimeter(self):
        return 2 * self.getWidth() * self.getHeight()

rect = Rect(1,2,4,5)
print(rect.getArea())
print(rect.getPerimeter())

