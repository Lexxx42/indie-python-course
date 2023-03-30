# Повторение - мать учения

# Каждый, кто смотрел Симпсонов, помнит, что в начале любой серии Барт писал забавные фразы на доске.
# Давайте и мы напишем подобную программу.

# На вход ей будет поступать фраза и затем количество раз, которое эту фразу нужно повторить.

# Sample Input 1:

# I am not smarter than the president
# 3
# Sample Output 1:

# I am not smarter than the president
# I am not smarter than the president
# I am not smarter than the president
# Sample Input 2:

# funny noises are not funny
# 2
# Sample Output 2:

# funny noises are not funny
# funny noises are not funny


print((input() + '\n') * int(input()), end='')
