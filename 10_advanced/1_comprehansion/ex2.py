d = (i**2 for i in range(1, 6))
a = list(d)
b = tuple(d)

print(a)
print(b)


d = (i ** 2 for i in range(1, 6))
#print(9 in d, 4 in d)
print(4 in d, 9 in d)
