from __future__ import unicode_literals
import glob
import sys
from hazm import *

CORPUS_PATHLIST = glob.glob('./HamshahriData/HamshahriCorpus/*/*.ham')
STOPWORD_PATH = './stopwords.txt'
deleting_words = ['.', '(', ')', ':', '»', '«', '،', '؛','!','؟']


def getInput():
    inp = input('کدوم بخش؟\n')
    if inp == '1':
        first_function()

    elif inp == '2':
        pass
    elif inp == '3':
        pass
    elif inp == '4':
        pass

    else:
        print('دوباره تلاش کنید!')
        getInput()


def first_function():
    inp = input(' "stopwords" or "input" ?')
    if inp == 'stopwords':
        showing_stopwords()
    elif inp == 'input':
        user_input()
    else:
        first_function()


def user_input():
    text = input('متن:\n')
    normalizer = Normalizer()
    normalized_text = normalizer.normalize(text)
    print('normalized:')
    print(normalized_text)
    normalized_text_tokens = word_tokenize(normalized_text)
    print('tokenized:')
    print(normalized_text_tokens)

    file = open(STOPWORD_PATH, 'r', encoding='utf-8')
    stop_words = file.read().split()
    file.close()
    stop_words.extend(deleting_words)
    words = [word for word in normalized_text_tokens if word not in stop_words]
    print('removing stopwords')
    print(words)

    stemmer = Stemmer()
    stemed_text_tokens = []
    for token in words:
        stemed_text_tokens.append(stemmer.stem(token))
    print('stemmed:')
    print(stemed_text_tokens)


def finding_stopwords():
    print('getting all of hamshahri posts paths')
    words_counter = {}

    for path in CORPUS_PATHLIST:

        file = open(path, 'r', encoding='utf-8')
        text = file.read()
        file.close()
        words = list(text.split())
        for word in words:
            if word in words_counter:
                words_counter[word] += 1
            else:
                words_counter[word] = 1

    list_of_words = sorted([(value, key) for key, value in words_counter.items()])
    stop_words_repeat = list_of_words[-40:]
    stop_words = {word for _, word in stop_words_repeat}
    print('saving stopwords:')
    open(STOPWORD_PATH, 'w').close()
    with open(STOPWORD_PATH, 'w', encoding='utf-8') as file:
        for word in stop_words:
            file.write(word + '\n')
        file.close()


def showing_stopwords():
    print('printing_stopwords:')
    file = open(STOPWORD_PATH, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    print(text)


getInput()
