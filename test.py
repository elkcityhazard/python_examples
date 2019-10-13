# asks for two numbers and determines if they divide evenly or not
#andrew m mccall

#define the function
def num_check():
        num = input("give me a number: ")
        check = input("give me another number: ")
        try: # exception handeling
            if num % check == 0: #check the numbers for even division
                print('This divides evenly. ')
            else:
                print('This does not divide evenly.')
        except (ZeroDivisionError, UnboundLocalError, NameError, ValueError, TypeError): #exception for these errors
            print('Invalid Operation')
while True: # initialize the loop
    num_check()

print('Thank you!')
