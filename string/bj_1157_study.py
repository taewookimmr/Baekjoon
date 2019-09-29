
from collections import Counter 
import operator
word = list(input().lower())
dic = Counter(word)
slist = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)
w, c = slist.pop(0)
if len(slist) == 0:
    print(w.upper())
else : 
    w2, c2 = slist.pop(0)
    if c == c2 :
        print('?')
    else:
        print(w.upper())

    

