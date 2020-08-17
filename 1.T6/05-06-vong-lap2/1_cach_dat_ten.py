#todo: Chuyển snake case --> camel case

#input: tong_so_tien
#output: tongSoTien

snakeName = input('Snake case: ')
#todo: camelName =????

arr = snakeName.split('_')
print(arr)
st = ''
for x in arr:
    xnorm = x[0].upper()+x[1:]
    st += xnorm + ''
    print(st)
print(st[0].lower() + st[1:])
