# Displaying input and if else condition functionality by Naman and boolean

# taking an input and adding into variable name
name = input("Hello buddy before you join, what is your name? ")

print("It's nice to meet you,", name)
answer = input(
    "Are you interested in joining? Please answer in capital letters ")
# basic if else evaluation
if answer == "YES":
    print("That's lovely to know!")
else:
    print("Oh no! That makes me sad!")
# now advanced if else usage.
# taking an input of integer format and adding into age and evaluating
age = int(input("Well, how old are you " + name + "? "))

if (age < 18):
    print("Well you are too young to register buddy", name)
elif (age > 60):
    print("You are too old sorry buddy")
else:
    print("Welcome! You are able to join", name)
