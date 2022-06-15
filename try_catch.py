# Displaying try and catch error functionality by Naman

try:
    ans = input("Well what should I divide 10 by?")
    num = int(ans)
    print(10 / num)
except ZeroDivisionError as e:
    print("Excuse me! You cannot divide by zero!")
except ValueError as e:
    print("You did not give me a valid number!")
    print(e)
finally:
    print("The final section always runs")
