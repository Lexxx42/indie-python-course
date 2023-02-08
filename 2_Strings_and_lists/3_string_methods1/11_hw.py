# На вход программе поступает строка,
# ваша задача вывести на экран индекс последней найденной латинской буквы a

# Если такого символа во введенной строке нет, выведите -1

# Sample Input 1:

# banana
# Sample Output 1:

# 5
# Sample Input 2:

# cat
# Sample Output 2:

# 1
# Sample Input 3:

# zoo
# Sample Output 3:

# -1

print(input().rfind("a"))
