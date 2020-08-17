def hanoi(N , src, dst, temp):
    if N == 1:
        print('Chuyển đĩa 1 từ  cọc', src, 'sang  cọc ', dst)
        return

    hanoi(N-1, src, temp, dst)
    print('Chuyển đĩa' , N ,  'từ  cọc', src, 'sang  cọc ', dst)    
    hanoi(N-1, temp, dst, src)          

N = 4
hanoi(N, 1, 3, 2)

