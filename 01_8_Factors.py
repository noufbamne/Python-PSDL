num = int(input("Enter a number: "))
if num > 0:
    print("Factors of", num, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    ("Please enter a positive number.")