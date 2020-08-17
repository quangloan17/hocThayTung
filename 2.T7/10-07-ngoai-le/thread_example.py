#thread_example.py
#Chạy tác vụ song song
from threading import Thread
import time

def task_function(i):
    time.sleep(2)
    print('Thực hiện tác vụ: ', i+1)

thr1 = Thread(target=task_function,args = [0])
thr2 = Thread(target=task_function,args = [1])

thr1.start()
thr2.start()
thr1.join();thr2.join();
print('======== Chương trình chính========')
