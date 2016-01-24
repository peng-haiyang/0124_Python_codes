#!/bin/python

###
print "\n"
print "*********\n" * 2
###

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.1f$."

print format_string % data

###
print "\n"
print "*********\n" * 2
###

s = "Hey there! what should this string be?"

print "Length of s = %d" % len(s)

print "The first occurrence of the letter a = %d" % s.index("a")

print "a occurs %d times" % s.count("a")

print "The first five characters are '%s'" % s[:5]
print "The next five characters are '%s'" % s[5:10]
print "The twelfth character is '%s'" % s[12]

print "The last five characters are '%s'" % s[-5:]

print "String in uppercase: %s" % s.upper()

print "String in lowercase: %s" % s.lower()

if s.endswith("ome!"):
	print "string ends with 'ome!'. Good!"

print "Split the words of the string: %s" % s.split(" ")


###
print "\n"
print "*********\n" * 2
###

number = 20
second_number = 0
first_array = [1,3,4]
second_array =[1,2]

if number > 15:
	print "1"

if first_array:
	print "2"

if len(second_array) == 2:
	print "3"

if len(first_array) + len(second_array) == 5:
	print "4"

if first_array and first_array[0] ==1:
	print "5"

if not second_number:
	print "6"

###
print "\n"
print "*********\n" * 2
###


numbers = [1, 2, 3, 4, 5, 6, 273, 274, 285]


for num in numbers:

	if num == 237:
		break

	if num % 2 == 1:
		continue

	print num
	
###
print "\n"
print "*********\n" * 2
###

def list_benefits():
	list_benefits = ['More organized code', 'More readable code', 'Easier code reuse']
#	print list_benefits
	return list_benefits

def build_sentence(benefit):
#	print "%s is a benefit of functions!" % benefit
	return "%s is a benefit of functions!" % benefit	

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
	print build_sentence(benefit)

#list_benefits()
name_the_benefits_of_functions()


###
print "\n"
print "****Classese and Objects*****\n" * 2
###

class MyClass:
	variable = "blah"

	def function(self):
		print "This is a message inside the class."

myobjectx = MyClass()
myobjecty = MyClass()
myobjecty.variable = "yackity"

print myobjectx.variable
print myobjecty.variable

myobjectx.function()

print "****Exercise*****\n" * 2

class Vehicle:
	name = ""
	kind = "car"
	color = ""
	value = 100.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000

print car1.name
print car2.color

print car1.description()
print car2.description()

###
print "\n"
print "****Dictionaries*****\n" * 2
###

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

for name, number in phonebook.iteritems():
	print "Phone number of %s is %d" % (name,number)

#
print "****Exercise*****\n" * 2
#

phonebook = {
	"John" : 938477566,
	"Jack" : 938377264,
	"Jill" : 947662781
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
	print "Jake is listed in the phonebook."
if "Jill" not in phonebook:
	print "Jill is not list in the phonebook."

###
print "\n"
print "****Modules and Packages*****\n" * 2
###

import re
all_fuc = dir(re)
print(all_fuc)

ans = 'find'
result = []

for word in all_fuc:
	if ans in word:
		 result.append(word)
	continue

print sorted(result, key=str.lower, reverse=True)
print(result)



