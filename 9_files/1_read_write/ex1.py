# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском

def file_read(file_name: str) -> None:
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        print(f.read())


file_read(file_name='test.txt')
