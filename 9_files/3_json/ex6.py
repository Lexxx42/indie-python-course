# Перед вами имеется программа, которая десериализует JSON строку к питоновскому значению
#
# Сама JSON строка оформлена неправильно, поэтому в программе возникает ошибка json.decoder.JSONDecodeError
#
# Ваша задача найти и исправить ошибки в оформлении  JSON строки. Остальную часть программы не нужно менять


import json

json_string = '''
{
    "customers": [
        {
            'userid': 123456,
            "username": "Allie Hsu",
            "phone": [
                "000-001-0002",
                "000-002-0002"
            ],
            "is_vip": true
        },
        [
            "userid": 223678,
            "username": "Donald Duck",
            "phone": null,
            "is_vip": false,
        ]
    ]
}
'''

data = json.loads(json_string)
print(data['customers'][0]['username'])
