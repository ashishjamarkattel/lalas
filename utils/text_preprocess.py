import re
import string
from html import unescape

import spacy

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from utils.acronyms import ACRONYMS_DICT
from utils.english_contractions import CONTRACTION_DICT

spacy_lemmatizer = spacy.load("en_core_web_sm", disable = ['parser', 'ner'])

def convert_to_lowercase(text):
    return text.lower()

def remove_whitespace(text):
    return " ".join(text.split())

def remove_punctuation(text):
    punct_str = string.punctuation
    punct_str = punct_str.replace("'", "") # discarding apostrophe from the string to keep the contractions intact
    return text.translate(str.maketrans("", "", punct_str))


def clean_html_tags(text):
    text = unescape(text)
    text = re.sub(r'<A HREF=".*?">.*?</A>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r',\d+$', '', text)

    return text.strip()

# Removing emojis
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags = re.UNICODE)
    return emoji_pattern.sub(r'', text)


def convert_acronyms(text):
    words = []
    acronyms_list = list(ACRONYMS_DICT.keys())
    for word in text.split():
        if word in acronyms_list:
            words = words + ACRONYMS_DICT[word].split()
        else:
            words = words + word.split()

    text_converted = " ".join(words)
    return text_converted


def convert_contractions(text):
    words = []
    contractions_list = list(CONTRACTION_DICT.keys())
    for word in text.split():
        if word in contractions_list:
            words = words + CONTRACTION_DICT[word].split()
        else:
            words = words + word.split()

    text_converted = " ".join(words)
    return text_converted

def remove_stopwords(text):
    stops = stopwords.words("english") # stopwords
    return " ".join([word for word in text.split() if word not in stops])

def text_lemmatizer(text):
    text_spacy = " ".join([token.lemma_ for token in spacy_lemmatizer(text)])
    #text_wordnet = " ".join([lemmatizer.lemmatize(word) for word in word_tokenize(text)]) # regexp.tokenize(text)
    return text_spacy

def discard_non_alpha(text):
    word_list_non_alpha = [word for word in text.split() if word.isalpha()]
    text_non_alpha = " ".join(word_list_non_alpha)
    return text_non_alpha

def text_normalizer(text):
    text = convert_to_lowercase(text)
    text = remove_whitespace(text)
    text = re.sub('\n', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = remove_punctuation(text)
    text = clean_html_tags(text)
    text = remove_emoji(text)
    text = convert_acronyms(text)
    text = convert_contractions(text)
    text = remove_stopwords(text)
    text = text_lemmatizer(text)
    text = discard_non_alpha(text)
    return text