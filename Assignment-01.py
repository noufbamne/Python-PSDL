"""
1. Check if the given number is even or odd.
num = int(input("Enter a positive number: "))
if num == 0:
    print("Number is zero.(It is an even number.)")
elif num > 0:
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
else:
    print("Please enter a positive number!")"""

"""2. Print Fibonacci Series
num = int(input("ENter the number of terms: "))
a = 0
b = 1
if num > 0:
    for i in range (num):
        print(a)
        c = a+b
        a = b
        b = c
else: 
    print("Please enter valid number of terms!")"""

"""4.Print factorial of a number
num = int(input("Enter the number to find the factorial: "))
fact = 1

if num > 0:
    for i in range (1, num + 1):
        fact = fact * i
    print("Factorial of", num,"is:", fact)

else:
    print("Please enter a positive number!")"""

"""
Write a program to reverse a number entered by the user.
num = int(input("Enter a number: "))
rev = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reversed number is:", rev)"""

"""6. Count the number of digits in a given integer.
num = int(input("Enter a number: "))
count = 0

if num == 0:
    print("Number of digits are: 1")
else:
    while num > 0:
        count = count + 1
        num = num // 10
    print("Number of digits are:", count)"""

"""num = int(input("Enter a number: "))

if num > 0:
    print("Factors of",num,"are:")
    for i in range (1, num + 1):
        if num % i == 0:
            print (i)
else:
    print("Enter a positive number")"""

"""num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits is:", sum)"""

'''start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))

if start > end:
    if(start % end == 0):
        print("Number is not prime number")

    else:
        print("Number is a prime number.")
else:
    print("Please enter a positive number.")'''

"""for i in range(1,6):
    for j in range(1, 5-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("* ", end="")
    print()"""

"""import random
random = random.randint(1, 20)
print("Guessing Game : Guess no. between 1 to 20 in three attempts !!!")
flag = 0
for i in range(1,4):
    num = int(input("Choose a number : "))
    if random == num:
        print("Hurrahh!!! You guessed right!!!")
        print("The number is", random)
        flag = 1
        break
    else:
        print("Try again!")
if flag == 0:
    print("The secret number was ",random)"""

n = int(input("Enter a positive integer for Collatz conjecture: "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print("Sequence:", end=" ")
    steps = 0

    while True:
        print(n, end="")
        if n == 1:
            break
        print("->", end="")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    print("\nTotal steps:", steps)
