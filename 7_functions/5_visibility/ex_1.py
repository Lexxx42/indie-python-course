# Напишите функцию, которая принимает имя и возраст водителя. Функция должна распечатать на экран заключение, может ли данный водитель управлять транспортом и определять она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE
#
# Если водитель может управлять, выведите фразу "<name> может водить" , в противном случае "<name> еще рано садиться за руль"
#
# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"


MIN_DRIVING_AGE = 18


def allowed_driving(name: str, age: int) -> None:
    bad = '{name} еще рано садиться за руль'
    good = '{name} может водить'
    print(bad.format(name=name) if age < MIN_DRIVING_AGE else good.format(name=name))


def allowed_driving1(name, age):
    print(f'{name} {["еще рано садиться за руль", "может водить"][age >= MIN_DRIVING_AGE]}')
