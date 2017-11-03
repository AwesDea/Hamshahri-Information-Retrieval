from __future__ import unicode_literals
from hazm import *

normalizer = Normalizer()
test = "چرا که نه آن ها هم می خواهم بدانم ی آمدم ببینم چه خبر شده است خوانداذه آهنگ موسیقی ترانه رایانه کامپیوتر"
print(test)
test1 = normalizer.normalize(test)
print(test1)
test2 = word_tokenize(test1)
print(test2)

stemmer = Stemmer()
for i in test2:
    s1 = stemmer.stem(i)
    print(s1,end=' -- ')

print()
lemmatizer = Lemmatizer()
for i in test2:
    l1 = lemmatizer.lemmatize(i)
    print(l1,end=' .. ')