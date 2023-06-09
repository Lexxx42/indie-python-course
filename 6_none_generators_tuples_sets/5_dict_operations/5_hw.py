# Перед вами словарь account
#
# Ваша задача сохранить в переменную keys список из всех ключей словаря account при помощи функции list
#
# В качестве ответа выведите переменную keys

account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}

print(keys := list(account.keys()))
