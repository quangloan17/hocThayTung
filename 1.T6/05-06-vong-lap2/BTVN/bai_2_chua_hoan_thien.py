xau = 'khu vực phía Tây Bắc Bộ và vùng núi phía Bắc do ảnh hưởng của vùng hội tụ gió trên 5.000m nên từ chiều tối, đêm và sáng sớm sẽ có mưa rào và dông rải rác, cục bộ có mưa vừa, mưa to. các khu vực còn lại cũng cần đề phòng mưa dông bất chợt từ chiều tối và đêm. trong cơn dông có khả năng xảy ra lốc, sét, mưa đá và gió giật mạnh. '

a = xau.split('.')
a =[x.strip(' ') for x in a]

for x in range(len(a)):
    if x == range(len(a)):
        if x[0].isalpha():
            x = ' ' + x[0].upper()+x[1:]
            print(x)
        else:
            print(x)
print(a)