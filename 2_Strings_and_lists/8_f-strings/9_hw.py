# Программа запрашивает у пользователя курс доллара - вещественное число,
# и также количество долларов(целое число), которое пользователь хочет приобрести.
# В итоге программа должна вывести следующее сообщение:

# Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
# You must pay <стоимость>

# Sample Input 1:

# 56.77
# 11
# Sample Output 1:

# Current dollar rate is 56.77. You want to buy 11 dollars
# You must pay 624.47
# Sample Input 2:

# 77.25
# 75
# Sample Output 2:

# Current dollar rate is 77.25. You want to buy 75 dollars
# You must pay 5793.75

print(f'Current dollar rate is {(rate:=input())}. You want to buy {(dollars:=input())} dollars\nYou must pay {float(rate)*int(dollars)}')