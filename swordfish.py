while True:
    name = input('What is your name?')
    if name != 'Andrew':
        continue
    password = input('Hello, Andrew.  What is the password? (It is a fish.)')
    if password == 'swordfish':
        break
print('Access Granted')
