"""
Create a program that (1.) asks the user for a number and then (2.) prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor of
26 because 26 / 13 has no remainder.)
"""
while True:
    num = int(input("Tell me a number: "))

    list_range = list(range(1, num+1))

    empty_list = []

    for number in list_range:
        if num % number == 0:
            empty_list.append(number)

    for n in empty_list:
        print(n)
    try_again = input("Do you want to go again? - type 'n' to exit: ")
    if try_again == 'n':
        break
