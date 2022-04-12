numbers = [0, 1, 2, 3, 4]

try:
    print(numbers[7])
except IndexError:
    print("Wrong index")

try:
    a = numbers[2]/numbers[0]
except ZeroDivisionError:
    print("Don't divide by 0")

try:
    liczby[3]
except NameError:
    print("This list doesn't exist")
