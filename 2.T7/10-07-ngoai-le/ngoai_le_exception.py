#Module bắt lỗi traceback.print_exc()
import traceback

def test():
    try:
        x = int(input('Nhập số x: '))
        y = int(input('Nhập số y: '))
        print('Tổng 2 số là:', x + y)
        return
    except:
        traceback.print_exc()#print('Lỗi xảy ra')
    finally:
        print('Đã nhập xong dữ liệu.')

    print('Chương trình tiếp tục')

test()
#finally là điểm tập kết 
