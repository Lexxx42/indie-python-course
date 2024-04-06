# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
# Ключ для декодирования располагается в json-файле.
# В качестве ответа нужно просто отправить получившийся текст.

# И обратите внимание, что раскодировать нужно только лишь буквы,
# все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.

# import json
#
#
# def json_read(file_name: str) -> dict:
#     with open(file=file_name, mode='r', encoding='utf-8') as f:
#         return json.loads(f.read())
#
#
# def file_read(file_name: str) -> str:
#     with open(file=file_name, mode='r', encoding='utf-8') as f:
#         return f.read()
#
#
# def decode_text(coded_text: str, code: dict[str, str]) -> str:
#     decoded = []
#
#     for letter in coded_text:
#         decoded.append(code.get(letter, letter))
#
#     return ''.join(decoded)
#
#
# alphabet = json_read(file_name='Alphabet.json')
# coded_text = file_read(file_name='Abracadabra__1_.txt')
#
# print(decode_text(coded_text=coded_text, code=alphabet))

import json

with open("Alphabet.json") as f:
    key = json.load(f)
with open("Abracadabra__1_.txt", encoding="utf-8") as f:
    txt = f.read()

print(txt.translate(txt.maketrans(key)))
