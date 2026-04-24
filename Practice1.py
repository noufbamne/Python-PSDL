def factorial(num):
    fact =1
    for i in range(1, num+1):
        fact = fact * i
    print("Factorial of", num,":",fact)
num_fact = int(input("Enter a number to find the factorial:"))
factorial(num_fact)



def add_elements(list):
    fruit = input("Enter fruit name:")
    list.append(fruit)

    ans = int(input("if you want to keep adding the elements enter 1 else enter 0:"))

    if ans == 1:
        add_elements(list)
    else:
        print(list)
        return
    
fruitlist =[]
add_elements(fruitlist)


def temp_convert(c):
    f = float(c * (9/5) + 32)
    return f

celcius = []
i = 0

while i < 3:
    c = float(input("Enter temperature to convert to farheneit"))
    celcius.append(c)
    i = i +1
farheneit = list(map(temp_convert, celcius))
print(farheneit)

from functools import reduce
num_list = [2, 3,4 ,5 ,6,7]
sum = reduce(lambda x, y: x+y, num_list, 0)
print(sum)
average = sum/len(num_list)
print(average)

employees =[
    {"id": 1, "Name" : "Nouf", "dept": "IT"},
    {"id": 2, "Name" : "Afu", "dept": "CS"},
    {"id": 3, "Name" : "Ansar", "dept": "IT"},
    {"id": 4, "Name" : "Nahal", "dept": "CS"},
    ]
it_list = list(filter(lambda emp : emp["dept"] == "IT", employees))
print(it_list)

square = lambda x : x*x
num = int(input("Enter a number to find the square:"))
num = abs(num)
print("Square is:", square(num))

str1 = input("Enter a string:")
reverse = str1[::-1]
print(reverse)