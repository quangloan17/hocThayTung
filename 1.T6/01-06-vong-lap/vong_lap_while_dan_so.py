# While là số liệu ngược lại với For, For là quá trình, While là kết quả

nam = 2020
danso = 97.3
r = 1.1/100

#TODO: Tìm năm dân số đạt mốc 120 triệu
while danso < 120:
    nam += 1
    danso = danso * (1+r) #Mỗi năm là dân số tăng hơn 1 năm trước
    print('Năm dân số vượt mức 120 triệu là: ', nam, 'Dân số thực tế là: ',round(danso,3))
