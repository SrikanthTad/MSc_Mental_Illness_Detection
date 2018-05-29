import openpyxl
import re
from nltk.corpus import stopwords
import spacy
from nltk import Tree
from nltk.stem.snowball import SnowballStemmer
import nltk
import string

obj = {
        'common': False,
        'personal': False,
        'long_count': False,
        'personal_check': False
    }

stop_words = stopwords.words('English')
common = ['scary', 'sleep', 'head', 'things', 'prolactin', 'night', 'echoes', 'antipsychotic', 'whispering', 'alone', 'insane',
          'dog bark', 'social', 'delusions', 'sad', 'television', 'tv', 'hallucinations', 'time', 'meds', 'symptoms',
          'voices', 'medication', 'cognitive', 'running', 'thoughts', 'mg', 'scared', 'psychosis', 'psychotic',
          'headaches','pace', 'pacing', 'voice', 'delusional', 'therapist', 'therapy', 'diagnosed',
              'pd', 'mri', 'chronic', 'zyprexa', 'schizophrenia', 'schizophrenic', 'voices', 'sz', 'daemon', 'fear',
              'paranormal', 'pain', 'abilify', 'sedating', 'smell', 'demons', 'soul', 'nicotine', 'doctor', 'traumatized',
          'telephone', 'ringing', 'agitation', 'light', 'stress', 'up', 'derealization', 'god', 'pdoc', 'dream', 'ra', 'problem', 'episodes',
          'feel', 'danger', 'insomnia', 'anxiety', 'disorder', 'sza', 'smoke', 'weight', 'antidepressants', 'adhd', 'concerta', 'clozapine',
          'dose', 'xanax', 'levitate', 'wonder', 'syndrome', 'ward', 'pill', 'depression', 'zopiclone', 'paranoia', 'normies', 'mood', 'depression', 'clutter' ]  # should be lowercase

personal = ["i", "my", "i've", "i'm", "im", "ive", "me", "mine"]  # should be lowercase
stemmer = SnowballStemmer("english")
nlp = spacy.load('en')

def filter_object(text):

    if not text:
        return obj
    else:
        # match = re.sub('(?<=\D)[.,]|[.,](?=\D)', '', text)
        match = re.split(r'\s+', text) #split by spaces
        #print(match)
    #check for start of sentence to identify personal comments
        if match[0].lower() in personal_roots:
            obj['personal'] = True
        count = 0

        for word in match:
            if word.lower() in common_roots: #lower the word to check against
                obj['common'] = True
            if ("mg" or "thought" or 'dreams') in word:
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
    if not text:
        return obj

    else:
        sent_text = nltk.sent_tokenize(text) #gives list of sentences
        # print(sent_text)
        for se in sent_text:
            #print(type(se))
            # don't need to apply special character removal since it's handled by spacy interpreter
            doc = nlp((se))
            sentences = next(doc.sents)
            # print(type(sentences))
            for word in sentences:
                print(word, word.dep_)
                if ((word.dep_ == 'nsubj' or 'nsubjpass' or 'poss') and (str(word).lower() in personal)):
                    obj['personal_check'] = True

        return obj

def filter(text):
    remove_list = ["szadmin", "szadmin's", "(szadmin)", "radmatech", "szadmin.", "szadmin:", "szadmin,", "sz admin",
                     "surprised j", "surprisedJ", 'surprisedj:', "surprisedj said:", " RowanAmethyst:", "RowanAmethyst", "szadmin,"]
    final_list = []
    s = 'null'
    #final_string_stemmed =[]
    final_list_stemmed = []

    if not text:
        return None
    else:
        tt = re.sub('['+string.punctuation+']', '', text)

        #tt = re.sub('(?<=\D)[.,]|[.,](?=\D)', '', text)
        new_text = re.split(r'\s+', tt)
        for word in new_text:
            if (word.lower()) not in remove_list:
                x = stemmer.stem(word)
                final_list_stemmed.append(x)
        final_string_stemmed = ' '.join(final_list_stemmed)
        print(final_string_stemmed)
        return final_string_stemmed

common_roots = []
personal_roots =[]


for c in common:
    common_roots.append((stemmer.stem(c)))
for p in personal:
   personal_roots.append(stemmer.stem(p))

te = "I'm sorry your mom calls you lazy...she must not be very understanding to your illness? tell her it's depression. maybe she'll let off.    "
te2="Right now my order is Invega 9mg, neurontin 500mg, lamictal 150mg, Wellbutrin XL 300mg. "
stemmed = filter(te)
go =filter_object(stemmed)
go = check_personal_comments(te)
print(go)


# def check_personal_comments(text):
#     # final_list_stemmed = []
#     # strip = re.split(r'\s+', text)
#     # for w in strip:
#     #     x = stemmer.stem(w)
#     #     final_list_stemmed.append(x)
#     # final_string_stemmed = ' '.join(final_list_stemmed)
#     sent_text = nltk.sent_tokenize(text) #gives list of sentences
#     # print(sent_text)
#     for se in sent_text:
#         #print(type(se))
#         # don't need to apply special character removal since it's handled by spacy interpreter
#         doc = nlp((se))
#         sentences = next(doc.sents)
#         # print(type(sentences))
#         for word in sentences:
#             if word.dep_ == 'nsubj' and (str(word).lower() in personal):
#                 obj['personal_check'] = True
#
#     return obj










