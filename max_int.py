#User inputs int
#Set int as highest_int
#Compare each new int to highest_int variable
#If new int is higher than highest_int, replace value with new int
#repeat until negative number is entered


# Fill in the missing code
max_int = 0
while True: #Compare each new number with max_int to see if its higher, if so replace it.
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int >= 0:
        if num_int > max_int:
            max_int = num_int
    else:
        break
print("The maximum is", max_int)    # Do not change this line
