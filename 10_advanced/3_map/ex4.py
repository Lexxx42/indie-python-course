# Помните задачку про RGB? Сейчас вам предстоит выполнить обратное преобразование
#
# Ваша задача создать функцию from_hex_to_rgb, которая принимает на вход строку - закодированный код цвета в формате RGB и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего). Вот посмотрите примеры:
#
# from_hex_to_rgb(#000000) => (0, 0, 0)
# from_hex_to_rgb(#FFFFFF) => (255, 255, 255)
# from_hex_to_rgb(#FF0000) => (255,0, 0)
# from_hex_to_rgb(#00FF00) => (0,255, 0)
# from_hex_to_rgb(#0000FF) => (0,0,255)
# from_hex_to_rgb(#FFFFFF) => (255,255,255)
# from_hex_to_rgb(#87CEEB) => (135,206,235)
# from_hex_to_rgb(#87CEFA) => (135,206,250)
# from_hex_to_rgb(#191970) => (25,25,112)
# Как только функция будет готова, ее необходимо применить ко всем элементам списка colors при помощи функции map. Ниже уже имеется готовый список colors и цикл обхода результата функции map. Добавьте только название функции внутри вызова map, все остальное код сделает за вас.
#
# Sample Input:
#
# Sample Output:
#
# Red=178, Green=34, Blue=34
# Red=220, Green=20, Blue=60
# Red=255, Green=0, Blue=0
# Red=255, Green=99, Blue=71
# Red=255, Green=127, Blue=80
# Red=205, Green=92, Blue=92
# Red=240, Green=128, Blue=128
# Red=233, Green=150, Blue=122
# Red=250, Green=128, Blue=114
# Red=255, Green=160, Blue=122
# Red=255, Green=69, Blue=0
# Red=255, Green=140, Blue=0
# Red=255, Green=165, Blue=0
# Red=255, Green=215, Blue=0
# Red=184, Green=134, Blue=11
# Red=218, Green=165, Blue=32
# Red=238, Green=232, Blue=170
# Red=189, Green=183, Blue=107
# Red=240, Green=230, Blue=140
# Red=128, Green=128, Blue=0
# Red=255, Green=255, Blue=0
# Red=154, Green=205, Blue=50
# Red=85, Green=107, Blue=47
# Red=107, Green=142, Blue=35
# Red=124, Green=252, Blue=0
# Red=127, Green=255, Blue=0
# Red=173, Green=255, Blue=47

def from_hex_to_rgb(code: str) -> tuple[int, int, int]:
    code = code.lstrip('#')
    return tuple(int(code[i:i + 2], 16) for i in (0, 2, 4))


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
          '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
          '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
          '#7CFC00', '#7FFF00', '#ADFF2F']

for red, green, blue in map(from_hex_to_rgb, colors):
    print(f"Red={red}, Green={green}, Blue={blue}")

