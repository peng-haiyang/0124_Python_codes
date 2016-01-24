#!/bin/python

###
print "\n"
print "*****list*****\n" * 2
###

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(names[1])

strings.append("Hello")
strings.append("World")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

###
print "\n"
print "*****Basic Operators*****\n" * 2
###


number = 1 + 2 * 3 / 4.0
print(number)
reminder = 11 % 3
print(reminder)
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
helloworld = "hello" + " " + "world"
print(helloworld)
lotsofhellos = "hello\n" * 10
print(lotsofhellos)
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print [1,2,3] * 3

print "\n"
print "*****exercise*****\n" * 2

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print len(x_list)
print len(y_list)
print len(big_list)

###
print "\n"
print "*****String Formatting*****\n" * 2
###

name = "John"
print "Hello, %s!" % name




