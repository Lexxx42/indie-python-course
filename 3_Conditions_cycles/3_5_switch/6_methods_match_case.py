# Использование методов в операторе match-case

# Вы можете спокойно вызывать методы объекта внутри оператора match-case

direction = 'NoRtH'
match direction.lower():
    case "north" | "east" | "south" | "west":
        print("Хорошо, я пошел!")
    case _:
        print("Неизвестное направление...")
