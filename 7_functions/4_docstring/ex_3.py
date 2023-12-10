# Шифр цезаря
# На основании предыдущей задачи мы с вами можем реализовать знаменитый шифр Цезаря. Этот шифр брал каждую букву исходной фразы и смещал ее на значение ключа, это так раз был на сдвиг. В пределах кодирования одной фразы значение сдвига всегда постоянно.
#
# И так, ваша задача создать функцию caesar_cipher , которая принимает на вход текст и значение сдвига.
#
# Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его по следующим правилам:
#
# если символ является знаком пунктуации, оставляем его как есть
# если это буква, то сместить ее при помощи ранее написанной функции shift_letter
# Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы
#
# caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
# caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
# Аннотации, мой друг, не забываем прописывать. И еще нужно сделать док-строку для функции caesar_cipher со значением «Шифр цезаря»
#
# Нужно написать только определение функций shift_letter и caesar_cipher
#
# Sample Input 1:
#
# lost in the echo
# 27
# Sample Output 1:
#
# mptu jo uif fdip
# Sample Input 2:
#
# from the inside
# 10
# Sample Output 2:
#
# pbyw dro sxcsno
# Sample Input 3:
#
# leave out all the rest
# -4
# Sample Output 3:
#
# hawra kqp whh pda naop
# Sample Input 4:
#
# one more light
# -33
# Sample Output 4:
#
# hgx fhkx ebzam

from string import ascii_lowercase


def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    return ascii_lowercase[(ord(letter) - ord('a') + shift) % 26]


def caesar_cipher(text: str, shift: int) -> str:
    """Шифр цезаря"""
    codded: str = ''
    for letter in text:
        if letter.isalpha():
            codded += shift_letter(letter=letter, shift=shift)
        else:
            codded += letter
    return codded


print(caesar_cipher('leave out all the rest', -1))
assert caesar_cipher('leave out all the rest', -1) == 'kdzud nts zkk sgd qdrs'
assert caesar_cipher('one more light', 3) == 'rqh pruh oljkw'
