from __future__ import unicode_literals
import glob
from hazm import *

CORPUS_PATHLIST = glob.glob('./HamshahriData/HamshahriCorpus/*/*.ham')
STOPWORD_PATH = './stopwords.txt'
deleting_words = [']', '(', ')', ':', '»', '«', '،', '؛', '!', '{', '}', '.', '@', '*', '#', '&', '$', '/', '_', '-',
                  '؟']

deleting_str = '[/?:">)(<.-_=+&$#@!.،؟»«'


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
    print('getting all of hamshahri posts words')
    words_counter = {}

    for path in CORPUS_PATHLIST:
        normalize = Normalizer()
        file = open(path, 'r', encoding='utf-8')
        text = file.readlines()
        text = ' '.join(text)
        text = normalize.normalize(text)
        text = word_tokenize(text)
        words = [wrd.strip() for wrd in text]
        for word in words:
            if word not in deleting_words:
                if word in words_counter:
                    words_counter[word] += 1
                else:
                    words_counter[word] = 1

        file.close()



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


def print_post( positional_index):
    for term in positional_index:
        print('a ' + term, end='-->\t')
        for doc in positional_index[term]:
            print(doc + " : " , sorted(positional_index[term][doc]), end='\t\t')
            print()
    return


def create_positional_index():
    print('getting all of hamshahri posts words for positional indexing')
    positional_index = {}
    doc_frequency = {}
    file = open(STOPWORD_PATH, 'r', encoding='utf-8')
    stop_words = [stp.strip() for stp in file.readlines()]

    path = CORPUS_PATHLIST[0]
    file = open(path, 'r', encoding='utf-8')
    text = [wrd.strip() for wrd in file.readlines()]
    text = ' '.join(text)
    file.close()

    normalizer = Normalizer()
    normalized_text = normalizer.normalize(text)
    normalized_text_tokens = word_tokenize(normalized_text)

    stop_words.extend(deleting_words)
    for i in range(len(normalized_text_tokens)):
        if normalized_text_tokens[i] not in stop_words:
            pass
        else:
            normalized_text_tokens[i] = None
    stemmer = Stemmer()
    stemed_text_tokens = []
    for token in normalized_text_tokens:
        if token is not None:
            stemed_text_tokens.append(stemmer.stem(token))

    # positional indexing
    # if word is not None:
    for i, word in enumerate(stemed_text_tokens):
        if word is not None:
            if word in doc_frequency:
                doc_frequency[word] += 1
            else:
                doc_frequency[word] = 1
            if word not in positional_index:
                positional_index[word] = {path: [i]}
            else:
                if path not in positional_index[word]:
                    positional_index[word][path] = [i]
                else:
                    positional_index[word][path].append(i)


    print(doc_frequency)
    print_post(positional_index)


# finding_stopwords()
create_positional_index()
# getInput()
