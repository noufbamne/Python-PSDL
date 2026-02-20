import random
n = int(input("Enter number of people in the group: "))
trials = int(input("Enter number of simulations (trials): "))
success = 0

# Run simulations
for x in range(trials):
# Generate random birthdays for n people (1 to 365)
    birthdayList = []
    for x in range(n):
        birthdayList.append(random.randint(1,365))
        # Check for duplicate birthdays by converting list to set
        if len(birthdayList) != len(set(birthdayList)):
                success += 1

# Calculate probability
probability = success / trials

print("\nEstimated Probability that at least two people share a birthday:")
print(round(probability,3))
print("Probability percentage : ",round((probability*100),2))

'''Output :
Enter number of people in the group: 23
Enter number of simulations (trials): 10000
Estimated Probability that at least two people share a birthday:
0.508
Probability percentage : 50.76'''