# В json-файле содержится информация о нескольких группах людей, при этом у каждой группы есть свой идентификатор.
#
# Ваша задача скачать файлик и самостоятельно найти идентификатор группы,
# в которой находится самое большое количество женщин, рожденных после 1977 года.
# В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин,
# рожденных после 1977 года.

import json
from typing import TypedDict


class GroupFemale(TypedDict):
    idx: int
    count_f: int


def file_read(file_name: str) -> dict:
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def find_female_groups_after_1977(data: dict) -> list[GroupFemale]:
    groups: list[GroupFemale] = []

    for group in data:
        idx = group['id_group']
        people = group['people']

        groups.append(
            GroupFemale(
                idx=idx,
                count_f=len([p for p in people if p['gender'] == 'Female' and p['year'] > 1977])
            )
        )

    return groups


def print_biggest_group(data: list[GroupFemale]) -> None:
    data.sort(key=lambda item: -item['count_f'])

    biggest_group = data[0]

    print(biggest_group['idx'], biggest_group['count_f'])


d = file_read(file_name='group_people.json')
print_biggest_group(data=find_female_groups_after_1977(data=d))
