# cho 1 số 1-999
# Yêu cầu: Đưa ra phát âm tiếng Việt của số đó:

lst = ['một','hai','ba','bốn','năm','sáu','bảy','tám','chín','mười']
lst2 = {1:'mốt',5:'lăm'}

def num2text1(d):
    return lst[d-1]

def num2text2(d):
    chuc = d//10
    donvi = d%10
    chuc_text,donvi_text = lst[chuc-1],lst[donvi-1]
    if donvi == 0: donvi_text = ''
    except_ = donvi == 5 or (donvi == 1 and chuc > 1)
    if except_:donvi_text = lst2[donvi]
    if chuc > 1:
        chuc_text + ' mươi ' + donvi_text
    else:
        return 'mười ' + donvi_text


for i in range(1,100):print(f'{i}-->{num2text2(i)}')


def num2text3(d):
    tram = d //100
    chuc = (d//10)%10
    donvi = d%10
    if chuc == 0:
        return ''
    else:
        return ''

def num2text(đ):
    if i <= d <= 10:
        return num2text1(d)

    if 11 <= d < 100:
        return num2text2(d)

    return num2text3(d)


