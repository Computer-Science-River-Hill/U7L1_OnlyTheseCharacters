# Setup Code
import module

# User input to build your list
myList = []

for x in range(5):
    nbr = int(input("Number: "))
    myList.append(nbr)

# User input for 1st number to find
nbr1 = int(input("Number to Find: "))

# User input for 2nd number to find
nbr2 = int(input("Number to Find: "))

answer = module.only(myList, nbr1, nbr2)
print(answer)
