# Группа методов is
# У строк есть целая группа методов, которая начинается на строку is.
# Все эти методы объединяет одно: они выполняют проверку и результат будет либо  True, либо False.

# Не забывайте, что строка - неизменяемый объект.
# Поэтому любой вызов метода строки не изменяет первоначальный объект.

# Метод islower
# Метод .islower  имеет следующий шаблон вызова:
# S.islower()
# Данный метод возвращает True ,
# если строка S не пустая и состоит только из алфавитных строчных(нижний регистр) букв.
# Если в строке имеется хотя бы одна заглавная буква, будет возвращено False.
# Все символы цифр или знак пунктуации игнорируются в проверках.

print("islower")
print(''.islower())
print('abcdefg', 'abcdefg'.islower())
print('abcDefG', 'abcDefG'.islower())
print('qwerty!', 'qwerty!'.islower())
print('12345', '12345'.islower())
print('12345abc', '12345abc'.islower())
print('12345aBc', '12345aBc'.islower())

# Метод isupper
# Метод .isupper  имеет следующий шаблон вызова:
# S.isupper()
# Данный метод возвращает True ,
# если строка S не пустая и состоит только из алфавитных заглавных(верхний регистр) букв.
# Если в строке имеется хотя бы одна строчная буква, будет возвращено False.
# Все символы цифр или знак пунктуации игнорируются в проверках.

print("\nisupper")
print(''.isupper())
print('ABCDEF', 'ABCDEF'.isupper())
print('ABCdEF', 'ABCdEF'.isupper())
print('QWERTY!', 'QWERTY!'.isupper())
print('12345', '12345'.isupper())
print('12345ZXC', '12345ZXC'.isupper())
print('12345ZxC', '12345ZxC'.isupper())

# Метод isdigit
# Метод .isdigit  имеет следующий шаблон вызова:

# S.isdigit()
# Данный метод возвращает True , если строка S не пустая и состоит только из десятичных цифр и символов,
# которые так же относятся к цифрам. В случае, если встретится другой символ, вернется False

print("\nisdigit")
print(''.isdigit())
print('0123456789', '0123456789'.isdigit())
print('0,1', '0,1'.isdigit())
print('0.1', '0.1'.isdigit())
print('qwerty', 'qwerty'.isdigit())
print('12a45', '12a45'.isdigit())

# Метод isalpha

# Метод .isalpha  имеет следующий шаблон вызова:
# S.isalpha()
# Данный метод возвращает True , если строка S не пустая и состоит только из букв.

print("\nisalpha")
print(''.isalpha())
print('ЗемфиРа', 'ЗемфиРа'.isalpha())
print('Я искала тебя', 'Я искала тебя'.isalpha())
print('Годами', 'Годами'.isalpha())
print('qwerty', 'qwerty'.isalpha())
print('12a45', '12a45'.isalpha())
print('qwerty!', 'qwerty!'.isalpha())

# Метод isalnum
# Метод .isalnum  имеет следующий шаблон вызова:

# S.isalnum()
# Данный метод возвращает True , если строка S не пустая и состоит только из букв и цифр.
# Если в строке имеется хотя бы один не буквенный и не числовой символ, то будет возвращено False

print("\nisalnum")
print(''.isalnum())
print('ЗемфиРа', 'ЗемфиРа'.isalnum())
print('Я искала тебя', 'Я искала тебя'.isalnum())
print('Годами', 'Годами'.isalnum())
print('qwerty', 'qwerty'.isalnum())
print('12a45', '12a45'.isalnum())
print('qwerty!', 'qwerty!'.isalnum())

# Метод istitle
# Метод .istitle  имеет следующий шаблон вызова:
# S.istitle()
# Данный метод возвращает True ,
# если строка S не пустая и является строкой заголовков:
# каждое новое слово начинается с заглавной буквы.

print("\nistitle")
print(''.istitle())
print('ЗемфиРа', 'ЗемфиРа'.istitle())
print('Хочешь солнце', 'Хочешь солнце'.istitle())
print('вместо лампы', 'вместо лампы'.istitle())
print('Хочешь', 'Хочешь'.istitle())
print('За Окошком Альпы?', 'За Окошком Альпы?'.istitle())
print('12345', '12345'.istitle())
