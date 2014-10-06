# Python the Hard Way - Exercise 6

x = "There are %d types of people." % 10 # displaying an integer
binary = "binary" # declaring a variable binary and assigning a string
do_not = "don't" # declaring a pointless string
y = "Those who know %s and those who %s." % (binary, do_not) #displaying strings in a larger string


print x #prints the value of the X string
print y # prints the value of the y string

print "I said: %r." % x #prints out the string in its single quotes
print "I also said: '%s'." %y #prints out string without embedded formatting

hilarious = False #correctly evaluates joke
joke_evaluation = "Isn't that joke so funny?! %r" #establishes a string that references another string but doesn't call it

print joke_evaluation % hilarious # calls the string

w = "This is the left side of ..." #declares a string
e = "a string with a right side." #declares another string

print w + e #concatenates the strings


