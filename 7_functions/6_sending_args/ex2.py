# Ваша задача создать функцию make_header, которая принимает
#
# обязательный параметр - строку, которую нужно обернуть в тег заголовка
# необязательный числовой параметр - уровень заголовка, по умолчанию принимает значение 1.
# Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня
#
# make_header('Нет') => '<h1>Нет</h1>'
# make_header('Bella Ciao', 4) => '<h4>Bella Ciao</h4>'
# make_header('Go little rock star', 6) => '<h6>Go little rock star</h6>'
# make_header('Девальвации не будет. Твердо и четко') => '<h1>Девальвации не будет. Твердо и четко</h1>'
# Ваша задача дописать только тело функции make_header
def make_header(word: str, level: int = 1):
    return f'<h{level}>{word}</h{level}>'


assert make_header('Нет') == '<h1>Нет</h1>'
assert make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
assert make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
assert make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'