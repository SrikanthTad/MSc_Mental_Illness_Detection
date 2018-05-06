import openpyxl
import re

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from nltk.probability import FreqDist
import nltk

EXCEL_IN = 'forum.filtered.xlsx'
#EXCEL_OUT = 'forum.filtered.xlsx'
slist = []
tlist=[]
flist =[]
legal_list =[]

stop_words = stopwords.words("english")

def filter_words(text):
    # if not text:
    #     return False
    match = re.split(r'\s+', text)
    return match





if __name__ == '__main__':    # Script starts here



    wb = openpyxl.load_workbook('forum.filtered.xlsx')
    ws = wb.get_sheet_by_name('Posts')
    mylist = []
    for row in ws.iter_rows('G{}:G{}'.format(ws.min_row, ws.max_row)):
        for cell in row:
            if (cell.value == None):
                pass
            else:
            # print ("Type: {}, Value: {}".format(type(cell.value), cell.value))
                for word in (cell.value.split()):
                    word = word.lower()
                    if word not in stop_words:
                        legal_list.append(word)

print(len(legal_list))
print("============================================SPLIT===============================================")

fdist = FreqDist(legal_list)
print(fdist.most_common(200))

