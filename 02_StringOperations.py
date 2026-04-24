str1 = "My name is Nouf."
print(str1)

print("Length of string str1:", len(str1))

str_rev = str1[::-1]
print("Reversed String:", str_rev)

str2 = "I am a good girl"
str3 = str1 + str2
print("After Concatenation: ", str3)

if str1 == str2:
    print("Equal Strings")
else:
    print("Not equal strings")

if 'Nouf' in str1:
    print("Substring found")
else:
    print("Substring not found")

uppercase = str.upper(str1)
print(uppercase)

print("Count of 'i: ", str1.count("i"))

print("Count of 'Nouf: ", str1.count("Nouf"))

string = input("Enter a sentence: ")
words = string.split()
for word in words:
    print(word, ":", len(word))

words = ["Cummins", "College", "Of", "Engineering", "for", "Women", "Pune"]
n = int(input("Enter the n:"))
print("Words geater than", n)
for word in words:
    if len(word)> n:
        print(word, ":", len(word))