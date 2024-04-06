from random import randint

d = (randint(1, 20) for i in range(7))

min(d)
sum(d)
# reversed(d) # TypeError: 'generator' object is not reversible
sorted(d)
# len(d) # TypeError: object of type 'generator' has no len()
max(d)
