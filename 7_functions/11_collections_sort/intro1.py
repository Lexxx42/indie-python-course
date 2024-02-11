heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87,
}

for key, value in sorted(heroes.items(), key=lambda item: item[1]):
    print(key, value)
# Batman 65
# Iron Man 65
# Aquaman 65
# Captain America 65
# Wonder Woman 70
# Flash 70
# Spider-Man 80
# Superman 85
# Hulk 87
# Thor 90
print('*' * 10)
heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87,
}

for k, v in sorted(heroes.items(), key=lambda item: (item[1], item[0])):
    print(k, v)
# Aquaman 65
# Batman 65
# Captain America 65
# Iron Man 65
# Flash 70
# Wonder Woman 70
# Spider-Man 80
# Superman 85
# Hulk 87
# Thor 90
