num = int(input("Enter a number: "))
num = abs(num)
count = 0
if num == 0:
    print("Number of digits are: 1")
else:
    while num > 0:
        count = count +1
        num = num // 10
    print("Number of digits are:", count)