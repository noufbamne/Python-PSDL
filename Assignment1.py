# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:33:28 2026

@author: ccoew
"""
"""
1. Check if the given number is even or odd.
num = int(input("Enter the positive number: "))

if num > 0:
    if num % 2 == 0:
        print("The given number" , num , "is an Even Number.")
        
    else:
        print("The given number" , num , "is an Odd Number.")

else:
    print("Please enter a positive number!")
    
Output:
    
    Enter the number: 2
    The given number 2 is an Even Number.
    
    Enter the positive number: -3
    Please enter a positive number!"""
    

"""
2. Print the pyramid pattern (using *).

rows = int(input("Enter number of rows:"))
if rows > 0:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end = "")
        print ("*" * (2 * i - 1))
        
else:
    print("Please enter valid number of rows!")
    
Output:
    
Enter number of rows:5
    *
   ***
  *****
 *******
*********

"""

"""
3. Print Fibonacci Series

n = int(input("Enter number of terms: "))
a, b = 0, 1

if n > 0:
    print("Fibonacci Series: ")
    for i in range(n):
        print(a)
        a, b = b, a + b
else:
    print("Please enter valid number of terms!")"""


"""
4.Print factorial of a number

num = int(input("Enter a positive number: "))

if num > 0:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", 5, "is:", fact)
else:
    print("Please enter a positive number > 0!")
    
Output:
Enter a number: 5
Factorial of 5 is: 120

Enter a number: -2
Please enter a positive number > 0! """

"""
5. Write a program to reverse a number entered by the user.
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    
    digit= num % 10
    rev = rev * 10 + digit
    num = num // 10
    
print ("Reversed number: ", rev)

Output:
    
Enter a number: 456789
Reversed number:  987654 """

"""
6. Count the number of digits in a given integer.

num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10
    
print("Number of digits:", count)

Output:

Enter a number: 12345678990
Number of digits: 11 """

import random

number = random.randint(1, 10)

print("Number guessing game! You will have three chances.")

for i in range (3):
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("Hurrahh!!! Correct Guess! Congratulationss. The number is:", number)
        break
    else:
        print("Try again")
        
print("Oopsss, Wrong Guess! The number was:", number, "Try again!")

"""
8. Find Factors of a Number

num = int(input("Enter a positive number > 0:"))

if num > 0:
    print("Factors of",num,"are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    print("Please enter a positive number > 0!")        
        
Enter a number:6
Factors of 6 are:
1
2
3
6
"""

"""
9. Sum of Digits in a Number

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print("Sum of digits:", sum)

Output:
Enter a number: 123
Sum of digits: 6

Enter a number: 123456
Sum of digits: 21 """

"""
10. Find Prime Numbers in the given Range
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers are: ")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            
Output:
Enter start range: 10
Enter end range: 20
Prime numbers are: 
11
13
17
19"""

