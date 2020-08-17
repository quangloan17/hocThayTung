def square(i):
    if i == 10:
        return i*i+1
    return i*i

def test_square(i):
    j = square(i)
    # if j != i*i:
    #     print('Error') #Điểm bẫy lỗi
    print(f'{i}*{i}={j}')

for i in range(100):
    test_square(i)

#Debug có 3 bước chính để bắt lỗi:
