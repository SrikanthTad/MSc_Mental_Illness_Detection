import pandas
import copy
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
import string
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier

commons = ['scary', 'sleep','hippocampus', 'head', 'prolactin', 'night', 'echoes', 'antipsychotic', 'whispering', 'alone', 'insane',
          'dog bark', 'social', 'delusions', 'sad', 'television', 'tv', 'hallucinations', 'meds', 'symptoms',
          'voices', 'medication', 'cognitive', 'running', 'thoughts', 'mg', 'scared', 'psychosis', 'psychotic',
          'headaches','pace', 'pacing', 'voice', 'delusional', 'therapist', 'therapy', 'diagnosed', 'counselor', 'pychologist',
          'pd', 'mri', 'chronic', 'zyprexa', 'schizophrenia', 'schizophrenic', 'voices', 'sz', 'daemon', 'fear',
          'paranormal', 'pain', 'abilify', 'sedating', 'smell', 'demons', 'soul', 'nicotine', 'doctor', 'traumatized',
          'telephone', 'ringing', 'agitation', 'light', 'stress', 'derealization', 'god', 'pdoc', 'dream', 'ra', 'episodes',
          'feel', 'danger', 'insomnia', 'anxiety', 'disorder', 'sza', 'smoke', 'weight', 'antidepressants', 'adhd', 'concerta', 'clozapine',
          'dose', 'xanax', 'levitate', 'wonder', 'syndrome', 'ward', 'pill', 'depression', 'zopiclone', 'paranoia', 'normies', 'mood', 'depression',
          'struggle', 'brain', 'daydream', 'schizoaffective', 'invega', 'provigil', 'geoden', 'seroquel', 'chlorpromazine', 'depixol', 'latuda', 'loxitane',
          'trifluperazine', 'prolixin', 'haloperidol', 'clonidine', 'mentally', 'stigma', 'schizos', 'paliperidone', 'selfmedicate', 'tomography', 'firstepisode']  # should be lowercase


data_source = pandas.read_excel('data.xlsx')
#stem each keyword
stemmer = SnowballStemmer("english")
stemmed_common = []
for word in commons:
    stemmed_common.append(stemmer.stem(word))

# with open('bags_of_words.txt', 'r') as f:
#     keywords = f.readline()
#
# keywords = keywords.replace("\n","")
# keywords = keywords.replace("'","")
# keywords = keywords.split(",")
# keywords = [o.replace(" ","") for o in keywords]
#
# print(keywords)

keywordsMap = {o:0 for o in stemmed_common}
# print(keywordsMap)

def convert_sentence_to_features(sentence):

    bag_of_words = copy.deepcopy(keywordsMap)
    for word in sentence:
        word = stemmer.stem(word)

        if word.lower() in bag_of_words:
            initial_value = bag_of_words[word.lower()]
            bag_of_words[word.lower()] = initial_value + 1

    return list(bag_of_words.values())

def get_result(user_predictions,user_labels):
  total_size = len(user_labels)
  correct = 0
  for i in range(total_size):
    if user_predictions[i] == user_labels[i]:
      correct += 1
  print("The accuracy is {}".format(correct * 1./total_size))


# ==========================================================
all_comments = list(data_source['Comment']) #Excel sheet

all_comments = [o for o in all_comments] #put all comments into array

all_comments_stemmed=[]
all_comments_last=[]
all_comments_nopunc=[]
for o in all_comments:
    new_stemmed = re.sub('['+string.punctuation+']', '', o)
    all_comments_nopunc.append(new_stemmed)
# print(all_comments_nopunc)


for o in all_comments_nopunc:
    all_comments_last.append(o.split(" "))

# print(all_comments_last)#tokenized all sentences


comment_features = [convert_sentence_to_features(sentence) for sentence in all_comments_last] #1010101010... one sentence at a time
comment_labels = [1 if o>2 else 0 for o in data_source["Ranking"]] #rank great than 2 then tag 1 else 0
# print(comment_labels)


#===================NAIVE BAYES==========================================

X_train, X_test, y_train, y_test = train_test_split(comment_features,comment_labels,test_size = 0.2)
# X_train = comment_features
# y_train = comment_labels
print(y_test)
print(X_test)


mnb = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
mnb.fit(X_train, y_train)
result = mnb.predict(X_test)
print(result)

accuracy = mnb.score(X_test, y_test)
print(accuracy)


plt.plot(result, "bo")
plt.plot(y_test, "ro")
plt.show()









#=====================USER CLASSIFIER=========================================

userMap = dict()

stemmed_sentences =[]
for user in data_source['User Id']:
    userMap[user] = []

for user in userMap:
    no_punc_sentences=[]
    sentences = list(data_source.loc[data_source['User Id'] == user]['Comment'])

    for o in sentences:

        y = re.sub('['+string.punctuation+']', '', o)
        # print(y)
        no_punc_sentences.append(y)

    sentences_split = [o.split(" ") for o in no_punc_sentences]

    sentences_split_words = [convert_sentence_to_features(o) for o in sentences_split]


    userMap[user] = sentences_split_words #make all that users words in dictionary of keywords present or no

user_labels = []
for user in userMap:
    overall_opinion = list(data_source.loc[data_source['User Id'] == user]['Overall Ranking Opinon'])[0]
    user_labels.append(overall_opinion) #grab all overall rankings


# chosen classifier
chosen_algorithm = mnb
user_features = [chosen_algorithm.predict(userMap[user]) for user in userMap] #make prediction
print(user_features)

for n in user_features:
    print(n)


#overall prediction based on all comment ratings
user_predictions = []
for n in user_features:
    if (1 in n):
        user_predictions.append(1)
    else:
        user_predictions.append(0)
# user_predictions = [1 if prediction ==1 else 0 for prediction in user_predictions]
print(user_predictions)


#compare with tagged results
#convert digits to 1 or 0 first
user_labels = [1 if label >2 else 0 for label in user_labels]
print(user_labels)

get_result(user_predictions, user_labels)


plt.plot(user_predictions, "bo")
plt.plot(user_labels, "ro")
plt.show()
# ========================================================================


