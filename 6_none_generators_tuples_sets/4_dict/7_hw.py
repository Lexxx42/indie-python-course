# Перед вами имеется словарь sweet
#
# Ваша задача:
#
# создать строковый ключ weight с целым значением 230
# создать строковый ключ have_topping c булевым значением True
# изменить значение ключа name на строку SuperCake
# изменить значение ключа calories на целое число 350
# В качестве ответа распечатайте в конце словарь sweet

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

sweet["weight"] = 230
sweet["have_topping"] = True
sweet["name"] = "SuperCake"
sweet["calories"] = 350
print(sweet)
