# Симпатичный узор
# На днях Иван у себя в прихожей выложил кафель,
# состоящий из квадратных черных и белых плиток.
# Прихожая Ивана имеет квадратную форму 4х4, вмещающую 16 плиток.
# Теперь Иван переживает, что узор из плиток, который у него получился, может быть не симпатичным.
# С точки зрения дизайна симпатичным узором считается тот,
# который не содержит в себе квадрата 2х2,
# состоящего из плиток одного цвета.
#
# Примеры возможных узоров:
#
# Симпатичный узор
#
# По заданному расположению плиток в прихожей Ивана требуется определить:
# является ли выполненный узор симпатичным.
#
# Программе поступает на вход 4 строки по 4 символа «W» или «B» в каждой,
# описывающие узор из плиток. Символ «W» обозначает плитку белого цвета, а «B» - черного.
#
# Ваша задача вывести «Yes», если узор является симпатичным и «No» в противном случае.
#
# Sample Input 1:
#
# BWBW
# BBWB
# WWBB
# BWWW
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# BBWB
# BBWB
# WWBW
# BBWB
# Sample Output 2:
#
# No

sp = []
for p in range(4):
    sp.append(list(map(str, input().split())))
if sp[0] == sp[1] or sp[2] == sp[3]:
    print("No")
else:
    print("Yes")
