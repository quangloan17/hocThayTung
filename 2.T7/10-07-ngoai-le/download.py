#args.py
import sys
import requests

if len(sys.argv) < 3:
    print('Usage:python download.py <url> <filename>')
url = sys.argv[1]
filename = sys.argv[2]
resp = requests.get(url)
with open(filename,'wb') as f:
    f.write(resp.content)
