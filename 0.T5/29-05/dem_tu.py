text = 'Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mươi mốt ngày'

text = text.lower()
for c in ['.', ',' , ':']:
   text = text.replace(c, ' ')

words_count = {}

for word in text.split():
   words_count[word] = words_count.get(word, 0) + 1

for word in words_count:
   print(word , ' : ', words_count[word])