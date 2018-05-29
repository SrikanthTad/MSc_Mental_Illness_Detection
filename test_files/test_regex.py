




import openpyxl
import re
from nltk.corpus import stopwords
import spacy
from nltk import Tree
from nltk.stem.snowball import SnowballStemmer
import nltk

EXCEL_IN = 'sample.xlsx'
EXCEL_OUT = 'sample.xlsx'

obj = {
        'common': False,
        'personal': False,
        'long_count': False,
        'personal_check': False
    }

#text = "Thanks Admin. My pdoc has told me the hippocampus, limbic system, and mesocortical pathways misfire in schizophrenics. SZ is so darn complex! "
text1 = " No. I've tried hard in the past + still do try. It's better on some days than others. Having my hair clean + looking good helps. "
text = "You remind me of my brother. He is a bit like you, in his room the whole day. Isn't your medication working properly? You shouldn't have to feel this way. "
stemmer = SnowballStemmer("english")

print(stemmer.stem("schizophrenia"))
print(stemmer.stem("schizophrenics"))
print(stemmer.stem("sza"))
print(stemmer.stem("sz"))


import string
match = re.sub('['+string.punctuation+']', '', text)
match = re.sub('(?<=\D)[.,+]|[.,+](?=\D)', '', text)

print(match)
tt = re.split(r'\s+', match)
print(tt)
final_list_stemmed =[]
for w in tt:
    x = stemmer.stem(w)
    final_list_stemmed.append(x)
    final_string_stemmed = ' '.join(final_list_stemmed)
print(final_string_stemmed)
print("=============")
newo = re.split(r'\s+', final_string_stemmed)
print(newo)


stop_words = stopwords.words('English')
common = ['scary', 'sleep', 'head', 'things', 'prolactin', 'night', 'echoes', 'antipsychotic', 'whispering', 'alone', 'insane',
          'dog bark', 'social', 'delusions', 'sad', 'television', 'tv', 'hallucinations', 'time', 'meds', 'symptoms',
          'voices', 'medication', 'cognitive', 'running', 'thoughts', 'mg', 'scared', 'psychosis', 'psychotic',
          'headaches','pace', 'pacing', 'voice', 'delusional', 'therapist', 'therapy', 'diagnosed',
              'pd', 'mri', 'chronic', 'zyprexa', 'schizophrenia', 'schizophrenic', 'voices', 'sz', 'smell', 'daemon', 'fear',
              'paranormal', 'pain', 'abilify', 'sedating', 'smell', 'demons', 'soul', 'nicotine', 'doctor', 'traumatized',
          'telephone', 'ringing', 'agitation', 'light', 'stress', 'up', 'derealization', 'god', 'pdoc', 'dream', 'ra', 'problem', 'episodes',
          'feel', 'danger', 'insomnia', 'anxiety', 'disorder', 'sza', 'smoke', 'weight', 'antidepressants', 'adhd', 'concerta', 'clozapine',
          'dose', 'xanax', 'levitate', 'wonder' ]  # should be lowercase

personal = ["i", "my", "i've", "i'm", "im", "ive", "me"]  # should be lowercase
stemmer = SnowballStemmer("english")
nlp = spacy.load('en')
common_roots = []
personal_roots =[]


for c in common:
    common_roots.append((stemmer.stem(c)))
for p in personal:
    personal_roots.append(stemmer.stem(p))

def filter_object(text):

    if not text:
        return obj
    else:
        # match = re.sub('(?<=\D)[.,]|[.,](?=\D)', '', text)
        match = re.split(r'\s+', text)
        #print(match)
    #check for start of sentence to identify personal comments
        if match[0].lower() in personal_roots:
            obj['personal'] = True
        count = 0

        for word in match:
            if word.lower() in common_roots: #lower the word to check against
                obj['common'] = True
            if "mg" or "thought" in word:
                obj['common'] = True
        #     if len(word) > 2 and (word not in stop_words):
        #         count += 1
        # if count > 2:
        #     obj['long_count'] = True

        return obj

def check_personal_comments(text):
    # final_list_stemmed = []
    # strip = re.split(r'\s+', text)
    # for w in strip:
    #     x = stemmer.stem(w)
    #     final_list_stemmed.append(x)
    # final_string_stemmed = ' '.join(final_list_stemmed)
    sent_text = nltk.sent_tokenize(text) #gives list of sentences
    # print(sent_text)
    for se in sent_text:
        #print(type(se))

        doc = nlp((se))
        sentences = next(doc.sents)
        # print(type(sentences))
        for word in sentences:
            print(word,word.dep_)
            if word.dep_ == 'nsubj' and (str(word).lower() in personal):
                obj['personal_check'] = True

    return obj







if __name__ == '__main__':    # Script starts here

    print("starting categorization using roots")
    ################################################setup variables###########################################################
    # stop_words = stopwords.words('English')
    # common = ['scary', 'sleep', 'my head', 'things', 'prolactin', 'night', 'echoes', 'antipsychotic', 'whispering', 'alone', 'insane',
    #       'dog bark', 'social', 'delusions', 'sad', 'television', 'tv', 'hallucinations', 'time', 'meds', 'symptoms',
    #       'voices', 'medication', 'cognitive', 'running', 'thoughts', 'mg', 'scared', 'psychosis',
    #       'headaches','pace', 'pacing', 'voice', 'delusional', 'therapist', 'therapy', 'diagnosed',
    #           'pd', 'mri', 'chronic', 'zyprexa', 'schizophrenia', 'voices', 'sz', 'smell', 'daemon',
    #           'paranormal', 'pain', 'abilify', 'sedating', 'smell']  # should be lowercase
    #
    # personal = ["i", "my", "i've", "i'm", "im", "ive", "me"]  # should be lowercase
    # stemmer = SnowballStemmer("english")
    # nlp = spacy.load('en')



    filter_object(final_string_stemmed)
    check_personal_comments(text)

    print(obj)
