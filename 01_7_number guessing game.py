import random
random = random.randint(1, 20)

print("Number guessing Gamee!!!")
print("Choose a number from 1 to 20. You have 3 guesses: ")
for i in range (1, 4):
    flag = 0
    num = int(input("Choose a number: "))
    if num == random:
        print("Huraahh you guessed right.")
        flag = 1
        break
    else:
        ("Try again")

if flag == 0:
    print("The number was", random)