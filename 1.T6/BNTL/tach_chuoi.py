s = '''Drew Doggett được biết đến là nhiếp ảnh gia, nhà làm phim nổi tiếng du lịch khắp thế giới. Trong hành trình của mình, anh thường ghi lại những phong cảnh, con người và văn hóa đặc sắc ở mỗi điểm dừng chân. Trong vương quốc huyền thoại là một trong những bộ ảnh mê hoặc nhất của anh cho đến nay. Bộ ảnh ghi lại vẻ đẹp có một không hai của những con ngựa đang rong ruổi khắp vùng đất băng đảo Iceland. Trong khi nhiều người lựa chọn những cảnh quan tuyệt đẹp ở Iceland để chụp, Doggett lại đi tìm mối liên kết giữa đàn ngựa hoang với thiên nhiên trong mỗi bức hình. Tới băng đảo, du khách có cơ hội chiêm ngưỡng loài ngựa này dọc tuyến đường vành đai.Giống ngựa Iceland được cho là loài ngựa Viking thuần chủng cao quý trên thế giới. Hơn 1.000 năm trước, những người từ Na Uy đã tới định cư đầu tiên trên băng đảo và mang theo một số con ngựa khỏe nhất trong đàn. Từ đó, chúng sống tách biệt ở đây và không bị lai tạo với bất kỳ giống ngựa nào khác.'''
d = []
c = 0
arr = s.strip().split(' ')
word = len(arr)
print(word)

for w in range(2,word+1,2):
    print(w, arr[w],arr[w+1])

for w in range(1,word+1,2):
    print(w, arr[w],arr[w+1])    
    