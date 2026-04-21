num = int(input("Enter a number: "))
rev = 0
temp = abs(num)
while temp > 0:
    
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if temp < 0:
    rev = -rev
print("Reverse of", num, "is", rev)