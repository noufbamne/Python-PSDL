list1 = ["Nouf", "Bhumika", "aboli"]
reversed_list = list(map(lambda x: x[::-1], list1))

print("Original list:", list1)
print("Reversed List:", reversed_list)

square = lambda x : x * x
num = int(input("Enter a number:"))
num = abs(num)
print("Square of number is:", square(num))

temp_list =[10, 20, 30, 99]
far_list = list(map(lambda x : (x * 9/5) + 32 , temp_list))
print("Farheniet list: ", far_list)

list2 = [1, 2, 3, 4,5 , 6, 7, 8, 9]
even_num = list(filter(lambda x : x % 2 == 0, list2))
print(even_num)

def prime(n):
    
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
prime = list(filter(prime, range (1, 21)))
print("Prime numbers:", prime)

from functools import reduce
if len(list2) != 0:
    average = (reduce(lambda x,y : x+y, list2))

    print ("average:", average)
else:
    print("List is empty")

students = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 73),
    ("David", 90)
]

passed = list (filter(lambda s: s[1]>= 50, students))
print("Passed:")

names = list(map(lambda s : s[0], students))
print("Names:", names)

total = reduce(lambda a, b: a+ b[1], students, 0)
print("total marks = ", total)

average = total/len(students)
print("Average Marks:", average)