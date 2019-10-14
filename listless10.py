# createa new list that are less than 6 in the original list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [] # empty list to hold numbers less than 6

for num in a: # the for loop to get all the numbers less than 6 and append them to the new list
    if num < 6:
        b.append(num)

print(b) # print out the smaller list


c = [item for item in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if item < 6 ] # list comprehension to check if item in list is less than 6

print(c)

# Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.

add_active = True
while True:
    try:
        user_number = int(input("Give me a number: "))
    except ValueError:
        print('The number you entered is not a valid entry.')
    d = [] #empty list to hold all the numbers less than the number given
    def user_list():
        for num in a: # more for loops
            if num < user_number: # check if num in a is less than the user given number
                d.append(num) # append the numbers that are less than the user given number to a new list
        print(d) # print out the new list
    user_list()
        # try_again = input("Do you want to try again? - type 'n' to quit ")
        # if try_again == 'n':
        #     break
        # else:
        #     add_active
