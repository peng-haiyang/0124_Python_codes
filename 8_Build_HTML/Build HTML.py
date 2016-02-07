print ("************" * 1)
print ("Build HTML")
print ("************\n" * 1)

temp = str(open('template.html','rU').read())

with open('southPark.csv','rU') as f:
    for line in f:
        temp_new = temp
        string = line.split(",")[0]
        filename = string.split()[-1]
        f = open('%s.html' % filename,'w')     
        for num,word in enumerate(line.split(","),1):  
            tobe_replace = 'VALUE'+str(num)  
            temp_new = temp_new.replace(tobe_replace,word)
        print(temp_new, file=f)
        f.close()

def write_file(string):
    filename = string.split()[-1]
    f = open('%s.html' % filename,'w')
    print(string, file=f)
    f.close()
    
