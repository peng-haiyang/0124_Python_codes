print ("************" * 1)
print ("Data Mining Google stock")
print ("************\n" * 1)

#name: get_data_list
#param: FILE_NAME <str> - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists <list>
def get_data_list(FILE_NAME):
    data_list = []
    with open(FILE_NAME) as ipf:
        for num,line in enumerate(ipf,1): ## to exclude the first line
            if num == 1:
                continue
            data_list.append(line.strip().split(','))
    return data_list

#name: get_monthly_averages
#param: data_list <list> - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list <list>
def get_monthly_averages(data_list):
    monthly_average_list = []
    data_list_my_sub = []
    for list in data_list:
        date_temp = list[0].split('/') 
        date = str("%02d-%s" %(int(date_temp[1]),date_temp[0]))
        if len(data_list_my_sub) == 0:
            vc = float(list[5]) * float(list[6])
            v = float(list[5])
            price = vc / v
            data_list_my_sub.append(date)
            data_list_my_sub.append("%.2f" % price)
            continue
        elif date == str(data_list_my_sub[0]):
            vc = vc + float(list[5]) * float(list[6])
            v = v + float(list[5])
            w = float(vc / v)
            price = float("%.2f" % w)
            data_list_my_sub[-1] = price
            continue
        monthly_average_list.append(data_list_my_sub)
        data_list_my_sub = []
        vc = float(list[5]) * float(list[6])
        v = float(list[5])
        price = vc / v
        data_list_my_sub.append(date)
        data_list_my_sub.append("%.2f" % price)
    monthly_average_list.append(data_list_my_sub)
    return monthly_average_list

#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info():
    monthly_average_list = get_monthly_averages(get_data_list('table.csv'))
    monthly_average_list.sort(key=lambda x:x[1])
    sorted_list = monthly_average_list
    best6_temp = sorted_list[-6:]
    worst6_temp = sorted_list[:5]
    best6 = []
    worst6 = []
    for list in best6_temp:
        a = list[0].split('-')
        Atuple = ("%02d-%s,%.2f" % (int(a[0]),int(a[1]),list[1]))
        best6.append(Atuple)
    for list in worst6_temp:
        a = list[0].split('-')
        Atuple = ("%02d-%s,%.2f" % (int(a[0]),int(a[1]),list[1]))
        worst6.append(Atuple)      
    f = open('output.txt', 'w')
    f.write("6 best months for Google stock:\n")
    for list in best6:
        f.write(str(list))
        f.write("\n")
    f.write("\n"*2)
    f.write("6 worst months for Google stock:\n")   
    for list in worst6:
        f.write(str(list))
        f.write("\n")
    f.close()
    
#get_monthly_averages(get_data_list('test.csv'))
print_info()

    
# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the 
# return in monthly_average_list

# call print_info function with the monthly_average_list from above 






