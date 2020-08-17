print('Phần mềm dự báo thời tiết')

a = float(input('Bạn nhập vào Nhiệt Độ: '))
b = float(input('Bạn nhập vào Tốc Độ Gió: '))
c = float(input('Bạn nhập vào Áp Suát Khí Quyển: '))

if a > 21:
    if b > 3:
        if c > 0.87:
            print('Mưa')
        else:
            print('Không mưa')
    else:
        print('Không mưa')
else:
    if b > 7:
        print('Mưa')
    else:
        if c > 1.04:
            print('Mưa')
        else:
            print('Không mưa')


