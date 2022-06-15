# Challenge 1
# implement a for loop that will iterate over the given names list and print out each name until it reaches the name John.
# You should also not print any names
# starting with letter M.

names = ["Adam", "Maria", "Kevin", "Madison", "John", "Bailey"]

for name in names:
    if name == "John":
        break
    elif name[0] != 'M':
        print(name)
#by putting names in a list, I placed condition of if and else when the name is John to just skip and if names that do not start with letter M to print.
