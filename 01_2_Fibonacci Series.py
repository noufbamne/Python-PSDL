num = int(input("Enter the number of terms: "))
a = 0
b = 1
if num > 0:
    print("Fibonacci Series: ")
    for i in range(1, num+1):
        print(a)
        c = a+b   
        a = b
        b = c
else:
    print("Please enter valid number of terms.")
