name = "Arbythecoder"
age = 25
location = "Earth"

def greet_user(name, age, location):
    print(f"Hello, {name}! You are {age} years old and live on {location}.")

greet_user(name, age, location)
def update_location(new_location):
    global location
    location = new_location
    print(f"Location updated to {location}.")
    greet_user(name, age, location)

update_location("Mars")
update_location("Venus")
# string , boolean , integer, float,list,dictionary 
#  a list is a collection  of items that can be changed while tuple is collection of times that cannot change.
# string

name ="Arbythecoder"
mother = "Adebimpe"
location = "ikeja"
# boolean
my_float = 0.14
my_perfect = 3.0
desktop =12.14
# boolean
boolean_value = True
listing =False
dealer = True


# arithimetic operations
new = 2 + 2
five_minus_three = 5 - 3
five_minus_one = 5 - 1

# comparison operations
five_greater_than_three = 5 > 3
five_less_than_thirty_three = 5 < 33
ten_equals_one = 10 == 1

# using type() to check the data types of each variable
naming  = type(name)
mothering = type(mother)

# what input() means
# input() is a built-in function in Python that allows you to take input from the user.
# It pauses the program and waits for the user to type something into the console.
hello = input("What's your name? ")
age = input("How old are you? ")



#convert age from string to integer
age = int(age)

# print welcome message
print(f"Hello {hello}, you are {age} years old.")

# erros gotten from adding a number to a string
name = "Arbythecoder" + age
# print(name)  # This will raise a TypeError because you cannot concatenate a string and an integer directly.