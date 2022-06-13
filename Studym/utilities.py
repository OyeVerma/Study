from .models import *
import csv

class CSV:
    def __init__(self, fromCSVobj: fromCSV):
        self.csvobj = fromCSVobj
        self.csvurl = fromCSVobj.file.url
    
    def savetoDB(self):
        csvfile = open(self.csvurl, 'r', encoding='utf-8')
        cont = csv.reader(csvfile)
        for r in cont:
            print(r)

