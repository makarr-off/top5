import sys
from collections import Counter

from bs4 import BeautifulSoup
import requests

name = sys.argv[1]

with open(name) as f:
    data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].replace("\n", "")


for i in range(len(data)):
    req = requests.get(data[i])
    soup = BeautifulSoup(req.text, "html.parser")
    s = soup.find('body')
    lst = s.get_text().upper().split()
    dct = {}
    c = Counter()
    for word in lst:
        c[word] += 1
    d = c.most_common(5)
    print(d)
