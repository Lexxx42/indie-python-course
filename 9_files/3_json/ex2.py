# Анализ продаж
# К вам в руки попал файлик формата json ,
# в котором содержится информация одного автосалона о продажах менеджеров.
# В файле указано для каждого менеджера список проданных им автомобилей,
# а также проставлена цена продажи каждого автомобиля.
#
# Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж.
# В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.
import json
from typing import TypedDict


class Seller(TypedDict):
    name: str
    sec_name: str
    sold: int


def file_read(file_name: str) -> dict:
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def find_sellers(data: dict) -> list[Seller]:
    sellers: list[Seller] = []

    for seller in data:
        manager = seller['manager']
        cars = seller['cars']

        sellers.append(
            Seller(
                name=manager['first_name'],
                sec_name=manager['last_name'],
                sold=sum([car['price'] for car in cars])
            )
        )

    return sellers


def print_best_seller(sellers_data: list[Seller]) -> None:
    sellers_data.sort(key=lambda item: -item['sold'])

    best_seller = sellers_data[0]

    print(best_seller['name'], best_seller['sec_name'], best_seller['sold'])


d = file_read(file_name='manager_sales.json')
print_best_seller(sellers_data=find_sellers(data=d))
