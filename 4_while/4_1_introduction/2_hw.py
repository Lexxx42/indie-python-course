# Напишите программу, которая распечатает все натуральные числа от 1000 до 2000 включительно.


# (lambda *args: [print(arg) for arg in args])(*range(1000, 2001))

# n = 1000
# while n <= 2000:
#     print(n)
#     n += 1

# number = 999
# while (number := number + 1) <= 2000: print(number)

print(*range(1000, 2001), sep='\n')
