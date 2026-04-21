num = int(input("Enter a number to find factorial:"))
fact = 1
if num > 0:
    for i in range(2, num +1):
        fact = fact * i

    print("Factorial of", num, "is :", fact)

else:
    print("Please enter a positive number.")
