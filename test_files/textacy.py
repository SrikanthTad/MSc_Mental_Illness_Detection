import textacy
import nltk
import textacy.datasets

obama_text = list(corpus.get(lambda doc: doc.metadata['speaker_name'] == 'Barack Obama'))
