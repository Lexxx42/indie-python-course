# Напишите программу, которая отсортирует список models по цвету в лексикографическом порядке (по алфавиту)
#
# Затем распечатайте элементы этого списка, каждый элемент на новой строке в формате:
#
# Производитель: <make>, модель: <model>, цвет: <color>
# Sample Input:
#
# Sample Output:
#
# Производитель: Nokia, модель: 216, цвет: Black
# Производитель: Honor, модель: 3, цвет: Black
# Производитель: Samsung, модель: 7, цвет: Blue
# Производитель: Mi Max, модель: 2, цвет: Gold
# Производитель: Huawei, модель: 4, цвет: Grey
# Производитель: Oppo, модель: 9, цвет: Red
# Производитель: Apple, модель: 10, цвет: Silver


models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    {'make': 'Apple', 'model': 10, 'color': 'Silver'},
    {'make': 'Oppo', 'model': 9, 'color': 'Red'},
    {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
    {'make': 'Honor', 'model': 3, 'color': 'Black'}
]

srt_colour = lambda x: x.get('color')
print_model = lambda x: print(
    f'Производитель: {x.get("make")}, модель: {x.get("model")}, цвет: {x.get("color")}'
)

models.sort(key=srt_colour)

for model in models:
    print_model(model)
