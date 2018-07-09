import openpyxl
import re
from nltk.corpus import stopwords
import spacy
from nltk import Tree
from nltk.stem.snowball import SnowballStemmer
import nltk
import numpy as np
import pandas
import copy
import string


common = ['scary', 'sleep','hippocampus', 'head', 'prolactin', 'night', 'echoes', 'antipsychotic', 'whispering', 'alone', 'insane',
          'dog bark', 'social', 'delusions', 'sad', 'television', 'tv', 'hallucinations', 'meds', 'symptoms',
          'voices', 'medication', 'cognitive', 'running', 'thoughts', 'mg', 'scared', 'psychosis', 'psychotic',
          'headaches','pace', 'pacing', 'voice', 'delusional', 'therapist', 'therapy', 'diagnosed', 'counselor', 'pychologist',
          'pd', 'mri', 'chronic', 'zyprexa', 'schizophrenia', 'schizophrenic', 'voices', 'sz', 'daemon', 'fear',
          'paranormal', 'pain', 'abilify', 'sedating', 'smell', 'demons', 'soul', 'nicotine', 'doctor', 'traumatized',
          'telephone', 'ringing', 'agitation', 'light', 'stress', 'derealization', 'god', 'pdoc', 'dream', 'ra', 'problem', 'episodes',
          'feel', 'danger', 'insomnia', 'anxiety', 'disorder', 'sza', 'smoke', 'weight', 'antidepressants', 'adhd', 'concerta', 'clozapine',
          'dose', 'xanax', 'levitate', 'wonder', 'syndrome', 'ward', 'pill', 'depression', 'zopiclone', 'paranoia', 'normies', 'mood', 'depression',
          'struggle', 'brain', 'daydream', 'schizoaffective', 'invega', 'provigil', 'geoden', 'seroquel', 'chlorpromazine', 'depixol', 'latuda', 'loxitane',
          'trifluperazine', 'prolixin', 'haloperidol', 'clonidine', 'mentally', 'stigma', 'schizos', 'paliperidone', 'selfmedicate', 'tomography']  # should be lowercase

stemmer = SnowballStemmer("english")
data_source1 = pandas.read_excel('Book1.xlsx')
data_source2 = pandas.read_excel('Book2.xlsx')
data_source3 = pandas.read_excel('Book3.xlsx')
common_stemmed =[stemmer.stem(c) for c in common]

rooted_1=[]
rooted_3=[]
all_comments = list(data_source1['strip'])
all_comments = [o for o in all_comments]

for o in all_comments:
    tt = re.sub('['+string.punctuation+']', '', o)
    rooted_1.append(tt)

rooted_2 = [t.split(" ") for t in all_comments]

for t in rooted_2:
    tt=str(t)
    ts = stemmer.stem(tt)
    rooted_3.append(ts)
print(rooted_3)
rooted_4 =[]




