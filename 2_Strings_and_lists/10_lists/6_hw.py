# Программа получает на вход список из целых чисел.
# Ваша задача найти среднее арифметическое введенного списка чисел

# Примечание:

# Чтобы прочитать из ввода целые числа и сохранить их
# в виде списка в переменной list_numbers вам необходимо написать строчку

# list_numbers = list(map(int, input().split()))
# Sample Input 1:

# 8 10
# Sample Output 1:

# 9.0
# Sample Input 2:

# 1 2 3
# Sample Output 2:

# 2.0

print(sum(lst := list(map(int, input().split()))) / len(lst))
