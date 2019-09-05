#Algorithm that prints the sum of the last 3 numbers in the sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter_int = 1
number1 = 1
number2 = 2
number3 = 3
current_number = 0

while counter_int <= n:
    if counter_int == 1: # If number entered is one of the first 3 numbers in the sequence, print them out
        print (number1)
    elif counter_int == 2:
        print (number2)
    elif counter_int == 3:
        print (number3)
    else: #If number entered is higher than the initial 3, run algorithm to find each new number in the sequence
        current_number = number1 + number2 + number3
        print (current_number)
        number1 = number2
        number2 = number3
        number3 = current_number
    counter_int += 1