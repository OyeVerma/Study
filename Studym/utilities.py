# from .models import *
import csv

# class CSV:
#     def __init__(self, fromCSVobj: fromCSV):
#         self.csvobj = fromCSVobj
#         self.csvurl = fromCSVobj.file.url
    
#     def savetoDB(self):
#         csvfile = open(self.csvurl, 'r', encoding='utf-8')
#         cont = csv.reader(csvfile)
#         for r in cont:
#             print(r)

def topicTextDecorator(text):
    lines = text.split('\n')
    result = ''

    if lines[0][0] == '*':
        result += f'<h1>{lines[0][1:].title()}</h1>'

    for line in lines:
        if line == '':
            continue
        if line[0:2] == '--':
            result += f'<li>{line[2:].title()}</li>'
        elif line[0] == '-':
            result += f'<li>{line[1:].title()}</li>'

    return(result)

h = '''*This is Hedding
-this is first li
--this is under first li
-this is second li
-this is third li
--this is under third li'''

topicTextDecorator(h)