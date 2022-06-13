import requests, json
from bs4 import BeautifulSoup

url = 'https://www.gktoday.in/topics/api/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

all_a = soup.findAll('a')
with open('all_a.json', 'w', encoding='utf-8') as f:
    f.write(str(len(all_a)))
    all_alist = {}
    for a in all_a:
        all_alist.update({a.text:a['href']})
        # f.write(a.text)
        # f.write(a['href'])
        # f.write('\n')
        # break
    f.write(json.dumps(all_alist))