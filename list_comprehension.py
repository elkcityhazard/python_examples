import random

a = list(random.sample(range(1000), 10))
print(a)
print([i for i in a if i % 2 == 0])
