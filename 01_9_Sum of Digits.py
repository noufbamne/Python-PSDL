number = int(input("Enter a number: "))
sum = 0
num = abs(number)

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print ("The sum of digits of number", number, "is:", sum)