def biggest_number(*args):
    print max(args)
    return max(args)


def smallest_number(*args):
    print min(args)
    return min(args)


def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-20, -5, 5, 100, 5, 7)
smallest_number(-10, -5, 5, 10, -33)
distance_from_zero(-88)

"""
Type()
"""

# Print out the types of an integer, a float,
# and a string on separate lines below.
print type(42)
print type(4.2)
print type('spam')

"""
import
"""

# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

# Import just the sqrt function from math on line 3!
# Now you can just type sqrt() to get the square root of a numbe no more math.sqrt()
# from module import function
# >>> from math import sqrt
# this is safe way

# Universal import can handle this for you. The syntax for this is:
# >>> from math import *
#  to import everything from the math
# not so safe as own function like sqrt() can mix for sqrt() from math import

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

"""
month day time 
"""

current_month = now.month
current_day = now.day
print current_year
print current_month
print current_day

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


# toka harkka
# my_string = "Tare on aika vahti koira!"
# print len(my_string)
# print my_string.upper()

"""
count meal costs with tax & tip
"""

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With 8 percent tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With 15 percent tip: %f" % bill
    return bill

meal_cost = raw_input("give meal cost ")
meal_cost_number = float(meal_cost)

meal_with_tax = tax(meal_cost_number)
meal_with_tip = tip(meal_with_tax)


"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay".
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:
"""

word = str.lower(raw_input("Give word  "))
if len(word) > 0 and  str.isalpha(word) == True:
    print (word)
elif len(word) == 0:
    print ("you gave just enter?")
elif str.isdigit(word)== True:
    print ("you gave numbers?")
elif str.isspace(word) == True:
    print ("That string is empty")
else:
    print ("you mixed numbers and letters or space")

word = str.lower(raw_input("Give word  "))
pituus = len(word)
new_word = word [1:pituus] + word [0]
print new_word
newest_word = new_word + 'ay'
print newest_word

"""
Henri's exercise 
"""

# raw_input \t =  tab \n =  next row
name = raw_input('What is your name?\t')
print  type (name)
print('Hi, %s.' % name)

# let's use raw_input 

kanta = raw_input("anna kolmion kanta mitta = ")
x = int (kanta)
korkeus = raw_input("anna kolmion korkeus = ")
y = int (korkeus)
yksikko = raw_input("anna mittayksikko mm,cm, dm,m,km = ")
pinta_ala = x * y/2
print "pinta-ala =", pinta_ala, yksikko + "2"

# let's use input as it is more clever

kanta = input("anna kolmion kanta mitta = ")
#  print type (kanta) --> int joten ei tarvitse erikseen muuttaa str -> int
korkeus = input("anna kolmion korkeus = ")
yksikko = raw_input("anna mittayksikko mm,cm, dm,m,km = ")
pinta_ala = kanta * korkeus/2
print "pinta-ala =", pinta_ala, yksikko + "2"

# the same exe with def 

def kolmion_ala (x,y, z):
    ala = x * y/2
    print "pinta-ala =", ala, z + "2"
    return ala

kanta = input("anna kolmion kanta mitta = ")
korkeus = input("anna kolmion korkeus = ")
yksikko = raw_input("anna mittayksikko mm,cm, dm,m,km = ")

kolmion_ala(kanta,korkeus,yksikko)

"""
def 
"""
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

"""
functions
"""

x = raw_input("how are you feeling now happy = h, sad = s ")

def speak(message):
    print message
    return message

if x == 'h':
    speak("I'm happy!")
elif x == 's':
    speak("I'm sad.")
else:
    speak("I don't know what I'm feeling.")
	
answer = raw_input("Shutdown yes/no ?  ")

def shut_down(s):
    print s
    return s

if answer == 'yes':
    shut_down("Shutting down")
elif answer == 'no':
    shut_down("Shutting aborted")
else:
    shut_down("Sorry")
	
	
"""
total city & car & hotel & spending money costs
"""

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    #print "car rental cost without discounts is", cost
    if days >= 7:
        cost -= 50
     #   print " 7 days or more you get 50 off. Cost is now ", cost
        return cost
    elif days >= 3 and days < 7:
        cost -= 20
     #   print " from 3 to 6 days you get 20 off.  Cost is now ", cost
        return cost
    else:
     #   print " no discounts. Cost is ", cost
        return cost

def hotel_cost(nights):
    return 140*nights

def spending_money(sum):
    return sum

def trip_cost(a, b, c):
    print "total cost is", plane_ride_cost(a) + rental_car_cost(b) + hotel_cost(b) + spending_money(c)
    return plane_ride_cost(a) + rental_car_cost(b) + hotel_cost(b)+ spending_money(c)

rental_city = raw_input("give planned city   ")
rental_days = int(raw_input("give car rental days  "))
spending_sum= int(raw_input("give spending sum  "))

trip_cost(rental_city, rental_days, spending_sum)

"""
list 
"""

zoo_animals = ["pangolin", "cassowary", "sloth", "monkey"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

"""
Slicing Lists and Strings
https://www.codecademy.com/courses/python-beginner-en-pwmb1/1/3?curriculum_id=4f89dab3d788890003000096
"""

suitcase = []
suitcase.append("sunglasses")# Your code here!

suitcase.append("shoes")
suitcase.append("hat")
suitcase.append("jeans")
suitcase.append("coat")


list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
print suitcase [0:2] # print 1st and 2nd item ['sunglasses', 'shoes']
print suitcase [2:5] # print 3rd ...['hat', 'jeans', 'coat']
print suitcase [2:3] # print ['hat']

bag = suitcase[1:4] #  We start at the index before the colon and continue up to but not including the index after the colon.
print bag # ['shoes', 'hat', 'jeans']

bag1 = suitcase[0:5] #  We start at the index before the colon and continue up to but not including the index after the colon.
print bag1 # ['sunglasses', 'shoes', 'hat', 'jeans', 'coat']

animals = "catdogfrog"

catx  = animals[:3]   # The first three characters of animals
dogx  = animals[3:6] # The fourth through sixth characters
frogx = animals [6:]  # From the seventh character to the end

print catx, dogx, frogx

animals = ["ant", "bat", "cat"]
print animals.index("bat")
animals.insert(1, "dog")
print animals
animals.insert(0, "frog")
print animals
cat_index = animals.index("cat")
animals.insert(cat_index,"cobra")
print animals

"""
for one and all
"""
my_list = [1,9,3,8,5,7]
my_list.sort()

for number in my_list:
    number = number *2
    print number

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal

start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    x = x ** 2
    square_list.append(x)

square_list.sort()
print square_list

"""
list index
"""
my_list = [1,9,3,8,5,7]
my_list.sort()

for number in my_list:
    number = number *2
    print number

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal

start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    x = x ** 2
    square_list.append(x)

square_list.sort()
print square_list

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # Prints Puffin's room number
print residents['Sloth']
print residents['Burmese Python']


"""
for loop 
"""

names = ["Adam","Alex","Mariah","Martine","Columbus"]
for x in names:
    print x

print names

"""
for loop on a dictionary to loop through its keys 
"""

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
# Note that dictionaries are unordered, meaning that any time you
# loop through a dictionary, you will go through every key, but you are
# not guaranteed to get them in any particular order.

# Use a for loop to go through the webster dictionary and print out all of the definitions.

for key in webster:
    print webster[key]
	
# print the whole dict
print webster

"""
Control Flow and Looping
"""
numbers = [1, 3, 4, 7]
for number in numbers:
    if number > 3:
        print number
print "We printed 7."

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
    if x % 2 == 0:
        print x
		
"""
Lists + Functions
"""

# we define a function count_small that has one argument, numbers.
# For each item n in numbers, if n is less than 10, we increment total.
# After the for loop, we return total.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

# After the function definition, we create an array of numbers called lost.
lost = [4, 8, 15, 16, 23, 42]
# We call the count_small function, pass in lost, and store the returned result in small.
small = count_small(lost)
#vFinally, we print out the returned result, which is 2 since only 4 and 8 are less than 10.
print small

# fizz count
def fizz_count(x):
    count = 0
    for variable in x:
        if variable == "fizz":
            count = count + 1
    return count


x = ["fizz", "cat", "fizz"]
count_total = fizz_count(["fizz", "cat", "fizz"])

print count_total

"""
String Looping
"""
# You can loop through strings the same way you loop through lists
for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i" or  letter == "m":
        print letter
		
"""
Python 2.7: Fibonacci series up to n
"""		
def fib(n):
#    a, b = 0, 1 similar as below
    a = 0
    b = 1
    while a < n:
        print a, b
        a, b = b, a+b

fib(100)  # Python 2.7: Fibonacci series up to n

for i in range(0, 22, 1):
    if i % 5 == 0:
        print i, " on jaollinen viidella"
 #        break
    else:
        print  i,  " ei oo jaollinen viidella"
else:
    print " ei oo", i

"""
raw_input & isalpha()
"""
#'Welcome to the Pig Latin Translator!'
name = raw_input("What's your name?  ")
print name
original = raw_input("Enter a word:  ")
if len(original) > 0 and original.isalpha() == True:
    print original
else:
    print ("That string is empty")
    # That string must have been empty
	


"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay".
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:
"""

word = str.lower(raw_input("Give word  "))
if len(word) > 0 and  str.isalpha(word) == True:
    print (word)
elif len(word) == 0:
    print ("you gave just enter?")
elif str.isdigit(word)== True:
    print ("you gave numbers?")
elif str.isspace(word) == True:
    print ("That string is empty")
else:
    print ("you mixed numbers and letters or space")


pituus = len(word)
new_word = word [1:pituus] + word [0]
print new_word
newest_word = new_word + 'ay'
print newest_word

"""
pig latin cose as it was in codeacademy 
"""
pyg = 'ay'

original = raw_input('Enter a word:')

word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
print new_word

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

	
"""
dict 
"""
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
n = [1, 2, 5, 10, 13]
print sum(n)
	
	
"""
dictionary is mutable
"""
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['Eggs'] = 5.0
menu['Chef salad'] = 7.5
menu['Coffee'] = 2.2
menu['Pizza'] = 9.8
menu['Beef with fries'] = 9.8


print "There are " + str(len(menu)) + " items on the menu."
print menu

"""
Dictionary  key xxxx : value yyyy
"""
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
# Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using 
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
# Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'.
zoo_animals['Rockhopper Penguin'] = 'Jungle House'

print zoo_animals

"""
dict remove & append
https://www.codecademy.com/courses/python-beginner-en-pwmb1/2/5?curriculum_id=4f89dab3d788890003000096
"""

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
beatles.append("xxx") # add xxx to dict
# print beatles

my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0] # print key fish value index 0 --> c

"""
dict append remove continue. we created a dictionary that holds many types of values.
"""
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
print inventory

# Add a key to inventory called 'pocket'
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# .sort() the items in the list stored under the 'backpack' key
inventory['backpack'].sort()
print inventory

# .remove('dagger') from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dagger')
# .append ('foo') t tho e list of items stored under the 'backpack' key
inventory['backpack'].append('foo')
print inventory

# Add 50 to the number stored under the 'gold' key
inventory['gold'] += 50
print inventory

"""
dict --> print key : value, count total 
"""

# key :  value -pair
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

# the same keys, we can loop through one dictionary and print values from both stock  and price
# Because you know that the prices and stock dictionary have the same keys, you can access
# the stock dictionary while you are looping through prices
# print format is following:
#    apple
#    price: 2
#    stock: 0
#
# For each key in prices, multiply the number in prices by the number in stock. 
# Print that value into the console and then add it to total
# Let's determine how much money you would make if you sold all of your food.

# For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
# Finally, outside your loop, print total.

total = 0
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    print "one fruit", prices[key] * stock[key]
    total = total + prices[key] * stock[key]
print total 


	
"""
dict making purchase
https://www.codecademy.com/en/courses/python-beginner-en-IZ9Ra/2/2?curriculum_id=4f89dab3d788890003000096
"""
# now you'rgoing to need to know how much you’re paying for all of the items on your grocery list.
 
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
	# function compute_bill that takes one argument food as input.
	# For each item in the food list, add the price of that item to total.

def compute_bill(food):
    total = 0
    for x in food:
        print x
        total += prices[x]
    print total
    return total

compute_bill(shopping_list)

"""
dict stocking out 
https://www.codecademy.com/en/courses/python-beginner-en-IZ9Ra/2/3?curriculum_id=4f89dab3d788890003000096
"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# While you loop through each item of food, only add the price of the item to total if the item's stock
# count is greater than zero.
# If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
def compute_bill(food):
    total = 0
    for x in food:
        if stock[x] > 0:
            print x
            total += prices[x]
            stock [x] -= 1
    print total
    print stock
    return total

compute_bill(shopping_list)



