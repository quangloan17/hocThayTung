x = float(input('Temperature: '))
y = float(input('Wind speed: '))
z = float(input('Bbarometric pressure: '))

if x > 21 and y < 3 :
    print('Không mưa')
elif (x > 21 and y > 3 and z > 0.87):
    print('Mưa')
if z < 0.87 and x > 21 :
    print('Không mưa')

if x < 21 and y > 7:
    print('Mưa')
elif (x < 21 and y < 7 and z > 1.04):
    print('Mưa')
if z < 1.04 and x < 21 :
    print('Không mưa')
