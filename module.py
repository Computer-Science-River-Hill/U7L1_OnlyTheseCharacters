# Write your function here
def only(myList, nbr1, nbr2):
    for x in myList:
        if x == nbr1 or x == nbr2:
            pass
        else:
            return False
    return True