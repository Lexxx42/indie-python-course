# Программа запрашивает у пользователя имя и фамилию,
# после чего выводит приветственное сообщение в следующем формате
# «Здравствуйте, <фамилия> <имя>!»

# Sample Input 1:

# Петя
# Иванов
# Sample Output 1:

# Здравствуйте, Иванов Петя!


(lambda name, second_name: print(f'Здравствуйте, {second_name} {name}!'))(input(), input())

# print(f'Здравствуйте, {" ".join([input() for _ in "12"][::-1])}!')
# print("Здравствуйте, {lastname} {name}!".format(name = input(), lastname = input()))
