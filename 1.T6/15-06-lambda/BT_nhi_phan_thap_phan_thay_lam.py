def bin2dec(s):
    if len(s) == 1:
        return int(s)
    return int(s[-1])*2 + bin2dec(s[:-1])

print(bin2dec('100011'))