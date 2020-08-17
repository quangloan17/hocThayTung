N = 50 #Số ký tự trong dòng không quá 50 ký tự.

f = open('input.txt',encoding='utf-8')
lines = f.readlines()
f.close()
d = []
for line in lines:
    while len(line) > 0:
        line = line.strip()
        pos = len(line)

        if pos > N:
            pos = N
            while pos > 0 and line[pos] != ' ':
                pos -= 1
            if pos == 0: #Không tìm được ký tự trắng
                pos = N
        d.append(line[:pos]+ '\n')
        line = line[pos:]

f = open('output.txt','w',encoding='utf-8')
f.writelines(d) #Thay thế vòng lặp for bằng writelines
f.close()