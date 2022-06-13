import requests, json
from bs4 import BeautifulSoup

url = 'https://www.gktoday.in/quizbase/current-affairs-quiz-june-2022'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

all_div = soup.findAll('div', attrs={'class':'sques_quiz'})

ls = []
t = open('dis.json', 'w', encoding='utf-8')

for div in all_div:
    question = div.text.split('[')[0]
    answer = div.text[div.text.find('Correct Answer: ')+len('Correct Answer: X '):div.text.find('Notes:')][1:-1]
    note = div.text[div.text.find('Notes:')+len('Notes:'):]

    options = []
    for o in div.text[div.text.find('['):div.text.find('Show Answer')].split('[')[1:]:
        options.append(o.split('] ')[-1])

    ls.append({
        'question':question,
        'options':options,
        'answer':answer,
        'note':note
        })
        
t.write(str(ls))

    