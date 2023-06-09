# Перед вами располагается словарь address
#
# Давайте проверим наличие следующих ключей:
#
# zip_code
# longitude
# post_code
# street_name
# number_house
# Программа должна проверить наличие ключей и вывести True, если ключ имеется,  или False, если ключ отсутствует.
#
# Проверки ключей должны выполняться в отдельной строчке в порядке перечисления ключей в задании

address = {
    "id": 7973,
    "uid": "42f2ce1d-90ab-4345-9595-0d9f42e6c085",
    "city": "East Monteland",
    "street_name": "Gusikowski Land",
    "street_address": "3230 Daugherty Centers",
    "secondary_address": "Apt. 562",
    "building_number": "58671",
    "mail_box": "PO Box 5313",
    "community": "Paradise Square",
    "zip_code": "58611",
    "zip": "01667",
    "postcode": "00563",
    "time_zone": "America/New_York",
    "street_suffix": "Burg",
    "city_suffix": "mouth",
    "city_prefix": "West",
    "state": "Wisconsin",
    "state_abbr": "NY",
    "country": "Mali",
    "country_code": "MH",
    "latitude": -56.97457993706476,
    "longitude": -104.29509072140858,
    "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715"
}

for item_to_check in ("zip_code", "longitude", "post_code", "street_name", "number_house"):
    print(item_to_check in address)
