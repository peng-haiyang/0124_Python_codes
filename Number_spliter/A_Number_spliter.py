print ("************" * 1)
print ("Number Spliter")
print ("************\n" * 1)

from functools import reduce


#### Define function ###
def get_number():
    global number
    while True:
        try:
            number = int(input("Please input a large whole number: "))
            if number < 0 :
                print("Forget to say, it must be a positive whole number")
                continue            
            break
        except ValueError:
            print("When I ask for a number, give me a number, come on!!")

def get_split():
    global split
    while True:
        try:           
            split = int(input("Please input the split (whole number): "))
            if split < 0:
                print("Forget to say, it must be a positive whole number")
                continue
            break
        except ValueError:
            print("When I ask for a number, give me a number, come on!!")


    
def spliter(x, sp):
    substr = ''
    outstr = ''
    j = sp
    k = str(x)
    count = 0
    com_i = ''
    com_j = ''
    for i in k:
        if k :
            substr = substr + k[:j]
            if outstr:
                outstr = outstr + ", " + substr
            else:
                outstr = outstr + substr
            com_j = com_i
            com_i = substr
            if com_j:
                if int(com_i) <= int(com_j):
                    count = 1
            com_i = k[:j]
            substr = ''
            k = k[j:]
        else:
            break
    print(outstr)
    if count:
        print("Sequence is not inceasing")
    else:
        print("Sequence is inceasing")
        
#### Function Definition Finished###

    
get_number()
get_split()

while True:
    while len(str(number)) % int(split) != 0:
        print ("%s must be evenly divisible by %d \nTry again." % (number,split))
        get_split()
    str(number).split()
    spliter(number,split)
    break









