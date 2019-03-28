import random

for i in range(5):
    spam = random.randint(1,10)
    print(spam)
    if spam == 1:
        print('Hello!')
    elif spam == 2:
        print('Howdy!')
    else:
        print('Greetings!')
