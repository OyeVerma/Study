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

import random
class TopicAPI:
    def __init__(self, text):
        self.text = text
    
    def title(self, random_title = 'Enter Title Here - '):
        if self.text[0] == '*':
            return self.text[1:self.text.find('\n')]
        else:
            random_title += str(random.randint(100000, 999999))
            return random_title

    def text(self):
        return self.text