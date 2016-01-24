#!/bin/python/

###
print "\n"
print "****Modules and Packages*****\n" * 2
###

import random
#help(random)

def lottery():
	for i in xrange(6):
		yield random.randint(1, 40)
		
	yield random.randint(1, 15)

for random_number in lottery():
	print "And the next number is... %d!" % random_number
#
print "****Exercise*****\n" * 2
#

def fib():

	a, b = 1, 1
	while 1:
		yield a
		a, b = b, a+b

import types
if type(fib()) == types.GeneratorType:
	print "Good, The fib function is a generator."

	counter = 0
	for n in fib():
		print n
		counter +=1
		if counter == 10:
			break

###
print "\n"
print "****List Comprehensions*****\n" * 2
###

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_lengths = []
for word in words:
	if word !="the":
		word_lengths.append(len(word))
print(word_lengths)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word !="the"]
print(word_lengths)

#
print "****Exercise*****\n" * 2
#

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(num) for num in numbers if num > 0]

print newlist

###
print "\n"
print "****Multiple Function Arguments*****\n" * 2
###

def foo(first, second, third, *therest):
	print "First: %s" % first
	print "Second: %s" % second
	print "Third: %s" % third
	print "And all the rest... %s" % list(therest)
foo(1,2,3,4,5,6,7)

def bar(first, second, third, **options):
	if options.get("action") == "sum":
		print "The sum is: %d" % (first + second + third)
	if options.get("number") == "first":
		return first

result = bar(1,2,3, action = "sum", number = "first")
print "Results: %d" % result

#
print "****Exercise*****\n" * 2
#

def foo(a, b, c, *d):
	return len(d)

def bar(a, b, c, **options):
	return options.get("magicnumber") == 7

if foo(1,2,3,4) == 1:
	print "Good."
if foo(1,2,3,4,5) == 2:
	print "Better."
if bar(1,2,3,magicnumber = 6) == False:
	print "Great."
if bar(1,2,3,magicnumber = 7) == True:
	print "Awesome!"











