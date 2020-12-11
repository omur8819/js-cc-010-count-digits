lower = int(input("Enter the lower bounds of the array: "))
higher = int(input("Enter the higher bounds of the array: "))
digit = int(input("Type the digit (between 0 - 9)"))
array = []

if (lower < 0 or higher < 0 or digit < 0):
    print("Please enter 0 or positive numbers!")

elif (lower > higher):
    print("Cannot be greater than the number of starts and ends of the sequence!")

elif (digit > 9):
    print("Please enter digit between 0 - 9!")

else:
    for i in range(lower, higher + 1):
        array.append(str(i))
    array = "".join(array)
    final = array.count(str(digit))
    print("The number {} is {} times in the {} - {} series.".format(digit, final, lower, higher))