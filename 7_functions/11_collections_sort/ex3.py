# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
# Предметы, имеющие одинаковые оценки, должны быть отсортированы в алфавитном порядке
#
# Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел
#
# Sample Input:
#
# Sample Output:
#
# Physics 93
# Programming 91
# Science 90
# Chemistry 88
# English 88
# Maths 88
# Art 78
# French 78
# History 78
from typing import Callable

subject_marks = [
    ('English', 88), ('Science', 90), ('Maths', 88),
    ('Physics', 93), ('History', 78), ('French', 78),
    ('Art', 78), ('Chemistry', 88), ('Programming', 91)
]

srt: Callable[[tuple[str, int]], tuple[int, str]] = lambda x: (-x[-1], x[0])
subject_marks.sort(key=srt)
print_grades: Callable[[tuple[str, int]], None] = lambda x: print(x[0], x[-1])
for item in subject_marks:
    print_grades(item)
