# various loops functionality by Naman

x = 0

# defining a while loop to print 0-10
while (x < 11):
    print(x)
    x = x + 1

# define a for loop to print 21-25
for x in range(21, 26):
    print(x)

# use a for loop over a collection
months = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul"]
for m in months:
    print(m)

# use the break and continue statements the following will break at 68
# Meaning it will display till 67 from 50
for x in range(50, 70):
    if (x == 68):
        break
    # if (x % 2 == 0): continue
    print(x)

# using the enumerate() function to get index
months = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul"]
for i, m in enumerate(months):
    print(i, m)
