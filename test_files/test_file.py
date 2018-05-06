import spacy
from nltk.corpus import stopwords
import openpyxl
import re
from nltk.corpus import stopwords
import spacy
from nltk import Tree
from nltk.stem.snowball import SnowballStemmer

words = ['changing', 'pace', 'pacing', 'ive', "i've", 'changling', 'convict', 'changed', 'medicated', 'medication']

stemmer = SnowballStemmer('english')
for w in words:
    print(stemmer.stem(w))

if __name__ == '__main__':
    for word in words:
        #print(word)
