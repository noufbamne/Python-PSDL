# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 14:41:38 2026

@author: ccoew
"""

'''org_list = [30, 10, 50, 30, 20, 50, 60, 90, 80, "Nouf", "Bhumika", "Aboli", "Sadia"]
print("Original List: ", org_list)

org_list.append(100)
print("After appending '100' to the original list", org_list)

org_list.insert(1, "new object at position 1")
print("After inserting an element at a position in the original list: ", org_list)

val = "new object at position 1"
org_list.remove(val)
print("After removing an element new object at position 1 from the original list: ", org_list)

org_list.remove("Nouf")
org_list.remove("Bhumika")
org_list.remove("Aboli")
org_list.remove("Sadia")
print (org_list)

print("Maximum element from the list is: ", max(org_list))
print("Minimum element from the list is: ", min(org_list))

print("Second max element:")
org_list.sort()
print(org_list[-2])

print("Original List: ", org_list)
new_list = [11, 22, 33, 44, 55]
print("New List:", new_list)

list1 = (org_list + new_list)
print("After Concatenation: ",list1)

rev_list = list1[::-1]
print("Original List: ", org_list)
print("Reversed List: ", rev_list)

set1 = set(list1)
print ("Unique number between 40 to 60 are:")
for i in set1:
    if 40<= i <= 60:
        print(i)
        
copy_list = list1.copy()
print("Copied list:", copy_list)

no_repeat = list(set(list1))
print("List without repeating elements:", no_repeat)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix 1: ", matrix1)
print("Matrix 2: ", matrix2)
print("Matrix Addition Result:", result)'''

#------------------------------------------------------------------------------

str1 = "My name is Nouf."
print("Original String: ", str1)

print("Length of the String:", len(str1))

rev_string = str1[::-1]
print("Original String: ", str1)
print("Reversed string:", rev_string)

print("Original String: ", str1)
str2 =" I am a good girl."
print("New String:", str2)

str3 =(str1 + str2)
print("After Concatenation of both the strings:", str3)

if str1 == str2:
    print("Strings are equal.")
else:
    print("Strings are not equal.")

if "Nouf" in str1:
    print("Substring found")
else:
    print("Substring not found")

str4 = str.upper(str3)
print("Uppercase:", str4)

print("Count of 'I'':", str4.count('I'))


print("Count of 'NOUF'':", str4.count('NOUF'))

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    print(word, ":", len(word))

words = ["Nouf", "is", "a", "student", "of", "Cummins", "College", "Of", "Engineering", "For", "Women", "Pune"]
n = int(input("Enter value of n: "))

print("Words longer than", n, ":")
for word in words:
    if len(word) > n:
        print(word)
