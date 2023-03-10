# Моржевый оператор

# Совсем недавно в мире Python, а именно начиная с версии python 3.8,
# появился Моржовый (walrus) оператор.
# Он дает возможность решить сразу две задачи:
# присвоить значение переменной и сразу получить это значение.
# Из-за этого можно написать код короче и сделать его более читаемым,
# и он может быть даже более эффективным с точки зрения вычислений.

# Что было до моржа?
# До этого оператора, если мы хотели вывести значение переменной,
# нужно было ее создать при помощи оператора присваивания = и затем вывести на экран.
# Все это занимало две строчки кода

see_walrus = 'Look at my walrus, my walrus is amazing'
print(see_walrus)

# Присваивать при помощи обычно оператора = внутри функции
# print не получится, будет ошибка TypeError

# Что теперь, когда есть «морж» ?
# Теперь мы можем выполнить присвоение и вывод ровно за одну строчку.
# И все благодаря «моржу», он просто красавчик.
# Сам оператор состоит из двоеточия и знака равно
# записанными слитно и выглядит вот так :=

# Свое название «морж» данный оператор получил за сходство с головой лежащего моржа.
# Да, есть в нем что-то похожее на моржа

print(see_walrus := 'Look at my walrus, my walrus is amazing')

print(see_walrus[:11] + 'horse')



