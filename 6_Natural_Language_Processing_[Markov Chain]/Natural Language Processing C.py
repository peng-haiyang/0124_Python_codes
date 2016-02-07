print ("************" * 1)
print ("Natural Language Processing C")
print ("************\n" * 1)

import random   

def markovChain_d(mylist):
    mc_d = {}
    i = 0
    for num,word in enumerate(mylist,1):
        if num<3:
            string_prev = mylist[0]+' '+mylist[1]
            continue ##break this loop, take next num
        #handle last word---
        if word == mylist[-1]:
            inputdic(string_prev,word,mc_d)
            inputdic(mylist[-2]+' '+mylist[-1],mylist[0],mc_d)
            inputdic(mylist[-1]+' '+mylist[0],mylist[1],mc_d)
            break
        #---
        inputdic(string_prev,word,mc_d)
        string_prev = mylist[num-2]+' '+mylist[num-1]
    return mc_d

def inputdic(string,word,d):
    if string not in keyList_dict(d):    
        d[string]=[word]
    else:
        d[string].append(word)
        d[string]=list(set(d[string]))    


def valueList_dict(d):
    mylist = []
    for key in d:
        mylist.append(d[key])
    return mylist

def keyList_dict(d):
    mylist = []
    for key in d:
        mylist.append(key)
    return mylist

def generate_txt(d, mylist):
    i = 1 # control the total looping times
    mystring = mylist[0]+' '+mylist[1]
    str_prv= mystring
    while i < 500 and True:
        str_aft=random.choice(d[str_prv]) #get the next word
        mystring = mystring + ' ' + str_aft #update the current whole string
        str_prv = str(mystring.split()[-2]) + ' ' + str_aft #update the current last two word string
        i +=1
    return mystring


while True:
    try:
        fn = input("Enter the text file name:")
        f = open(fn,'r')
        mylist=f.read().split()
        f.close()
        print(mylist)
        print("----------------")
        d = markovChain_d(mylist)
#        for key in d:
#            print("%s--%s" % (key,d[key]))
        results=generate_txt(d, mylist)
        print("The results:\n--------------\n",results)
        f.close()
        fn_op = input("Enter file name to write output to <Enter to skip>:") 
        if fn_op:
            f_op = open(fn_op,'w')
            print(results, file=f_op)
            f_op.close()
            break
        break
    except ValueError:
        print("please try again")



