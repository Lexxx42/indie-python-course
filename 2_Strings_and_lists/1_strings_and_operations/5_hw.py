# Напишите программу, которая сначала считывает две фразы по очереди,
# а потом воспроизводит их в той же последовательности, каждую на отдельной строчке.

# Sample Input 1:

# Hello!
# Hi!
# Sample Output 1:

# Hello!
# Hi!
# Sample Input 2:

# Привет
# Пока
# Sample Output 2:

# Привет
# Пока

# (lambda x, y: (print(x, y, sep='\n')))(input(), input())

print(input(), input(), sep='\n')
