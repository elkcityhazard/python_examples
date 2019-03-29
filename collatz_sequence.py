#define the collatz sequence function

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
try:
    n = input("Please enter a number: ")

    while n != 1:
        n = collatz(int(n))
except ValueError:
    print("You must enter a valid whole number.")
