print ("************" * 1)
print ("TagCloud2")
print ("************\n" * 1)

import string
from htmlFunctions import make_HTML_box
from htmlFunctions import make_HTML_word
from htmlFunctions import print_HTML_file

#punctuation
def punct(mylist):
    new_list = []
    for st in mylist:
        for punch in string.punctuation:
            st = st.replace(punch,"")
        new_list.append(st)
    return new_list

#input file as a list
def listwords(filename):
    with open(filename,'r') as f:
        results = f.read().split()
    return results

#remove stopwords, return a new list
def remove_sw(filename,stopwords):
    fn = punct(listwords(filename))
    sw = listwords(stopwords)
    for word in sw:
        for item in fn:
            if word.lower() == item.lower():
                fn.remove(item)
    for w in punct(fn):
        if w == '':
            fn.remove(w)
    return fn

#extract all the words by Obama (after tag'PRESIDENT OBAMA')
#stop once when meet 'MR. ROMNEY' or 'MR. LEHRER'
def word_of_Obama(wordlist):
    wl_obama = []
    a=0
    tag = 0
    for num,word in enumerate(wordlist,0):
        if word == 'PRESIDENT' and wordlist[num+1] == 'OBAMA':
            a = num+2
            tag = 1
        if tag and word == 'MR' and wordlist[num+1] in ['ROMNEY','LEHRER']:
            b = num
            for w in wordlist[a:b]:
                wl_obama.append(w)
            a = num + 2
            tag = 0
    return wl_obama

#extract all the words by Obama (after tag'PRESIDENT OBAMA')
#stop once when meet 'PRESIDENT OBAMA' or 'MR. LEHRER'
def word_of_Romney(wordlist):
    wl_obama = []
    a=0
    tag = 0
    for num,word in enumerate(wordlist,0):
        if word == 'MR' and wordlist[num+1] == 'ROMNEY':
            a = num+2
            tag = 1
        if tag and word in ['MR', 'PRESIDENT'] and wordlist[num+1] in ['OBAMA','LEHRER']:     
            b = num
            for w in wordlist[a:b]:
                wl_obama.append(w)
            a = num + 2
            tag = 0
    return wl_obama

#wordlist = ['apple', 'bear', 'apple', 'lemon']

#return a dictionary for word count
def d_word_count(wordlist):
    new_list = []
    for word in wordlist:
        new_list.append(word.lower()) 
    d = {}
    for word in new_list:
        if not d:
            d[word] = 1
            continue
        key_list =[key for key in d]
        if word in key_list:
            d[word] +=1
            continue
        d[word] = 1
    return d

d_Obama = d_word_count(word_of_Obama(remove_sw('debate.txt','stopWords.txt')))
d_Romney = d_word_count(word_of_Romney(remove_sw('debate.txt','stopWords.txt')))


def ls_wc(d):
    ls_tuple = []
    for key in d:
        tuple_ = (d[key],key)
        ls_tuple.append(tuple_)
    ls_tuple.sort()
    ls_tuple.reverse()
    new_list = []
    for num,t in enumerate(ls_tuple,1):
        if num <=40:
            a = (t[1],t[0])
            new_list.append(a)
    new_list.sort()
    return new_list    

def ls_convert(mylist):
    new_list = []
    for num,t in enumerate(mylist,1):
        if num <=40:
            a = str("%s:%s" % (t[0],t[1]))
            new_list.append(a)
    return new_list    

print("------------------------")

for fn in ['Obama', 'Romney']:
    if fn == 'Obama':
        pairs = ls_wc(d_Obama)
    else:
        pairs = ls_wc(d_Romney)   
    high_count=20
    low_count=2
    body=''
    for word,cnt in pairs:
        body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    print_HTML_file(box,fn)  # writes HTML to file name 'testFile.html'








