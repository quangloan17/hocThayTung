def count_char(st,c):
    count = 0
    for ch in st:
        if c == ch:
            count += 1
    return count

print(count_char('aaaaaaaaaaaaa','a'))

