s = 'Khu vực phía Tây Bắc Bộ và vùng núi phía Bắc do ảnh hưởng của vùng hội tụ gió trên 5.000m nên từ chiều tối, đêm và sáng sớm sẽ có mưa rào và dông rải rác, cục bộ có mưa vừa, mưa to. Các khu vực còn lại cũng cần đề phòng mưa dông bất chợt từ chiều tối và đêm. Trong cơn dông có khả năng xảy ra lốc, sét, mưa đá và gió giật mạnh'

a = s.split(".")
print(a)
s1=""
for x in a:
    if x == a[0]:
        if x[0].isdigit():
            s1 += x
        elif x[0].isalpha()  :
            s1 +=x[0].upper() + x[1:]
    else :
        if x[0].isdigit() :
            s1+="."+ x
        elif x[0].isalpha() :
            s1+=". " + x[0].upper() + x[1:]
        elif x[0] == " " and x[1].isalpha() :
            s1 += ". " + x[1].upper() + x[2:]
        elif x[0]==" " and x[1].isdigit() :
            s1 +="." + x
print(s1)
    
    
