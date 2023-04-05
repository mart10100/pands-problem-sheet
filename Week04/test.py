#test.py

number = int(input("Please enter a positive integer: "))

while (number % 2 != 0 and number > 1):
    print(int(number))
    number = ((number * 3) + 1)
    while (number % 2 == 0 and number > 1):
        print(int(number))
        number = (number / 2)
        while (number % 2 != 0 and number > 1):
            print(int(number))
            number = ((number * 3) + 1)
        