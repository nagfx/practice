# Displaying functions functionality by Naman

# mixing dough steps
def mixing_dough():
    print("Firstly mix ingredients in bowl")
    print("Secondly add water as needed")
    print("Thirdly use the mixer to make the dough")

# washing car steps with function taking a parameter


def washing_car(amount_paid):
    # Carrying out function based on amount paid
    if (amount_paid >= 10):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    elif (amount_paid < 10):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry")


mixing_dough()

print("First time")
mixing_dough()
print("Now the last time")

# storing int value in payment
payment = int(input("How much will you pay? "))
# calling function and passing the payment value in payment function
washing_car(payment)
