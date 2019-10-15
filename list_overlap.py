import random

a = list(range(1, random.randint(1, 1000)))
b = list(range(1, random.randint(1, 1000)))
c= []
for i in a:
    if i in b:
        if i not in c:
            c.append(i)

print(c)
print("\n\t")

# my one line answer
print(set(a).intersection(b))
