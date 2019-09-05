#Algorithm that prints the sum of the last 3 numbers in the sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter_int = 1
number1 = 1
number2 = 2
number3 = 3
current_number = 0

while counter_int <= n:
    if counter_int == 1:
        print (number1)
    elif counter_int == 2:
        print (number2)
    elif counter_int == 3:
        print (number3)
    else:
        current_number = number1 + number2 + number3
        print (current_number)
        number1 = number2
        number2 = number3
        number3 = current_number
    counter_int += 1