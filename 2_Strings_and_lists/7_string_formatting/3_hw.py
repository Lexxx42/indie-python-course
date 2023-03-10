# Напишите программу, которая считывает целое число,
# и затем сообщает какие числа будут следующим и предыдущим в определенном формате.
# Пробелы, знаки препинания, заглавные и строчные буквы важны!

# Sample Input:

# 99
# Sample Output:

# Для числа 99 предыдущим будет число 98.
# Для числа 99 следующим будет число 100.

print(f"""
Для числа {(number := int(input()))} предыдущим будет число {number - 1}.
Для числа {number} следующим будет число {number + 1}.
""")

# print(f'Для числа {(n:=int(input()))} предыдущим будет число {n-1}.\nДля числа {n} следующим будет число {n+1}.')
