import subprocess
#os.system('calc.exe') #firefox
#os.system('ping google.com')

result = subprocess.getoutput('ping googe.com')
#print(result)

for line in result.split('\n'):
    pos = line.find('time=')
    if pos >= 0:
        print(line[pos:])
