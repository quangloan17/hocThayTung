#todo: Chuyển snake case --> camel case

#input: tong_so_tien
#output: tongSoTien

camelName = input('Camel case: ')
#todo: camelName =????

st = ''

N = len(camelName)
for i in range(N):
    c = camelName[i]
    if c.isupper():
       st += '_' 
    st+=c.lower()
print(st)
