# Напишите программу, которая отсортирует список subject_marks по возрастанию оценок. Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел
#
# Sample Input:
#
# Sample Output:
#
# History 82
# English 88
# Science 90
# Physics 93
# Maths 97

from typing import Callable

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
srt_second_val: Callable[[tuple[str, int]], int] = lambda x: x[-1]
subject_marks.sort(key=srt_second_val)
print_grades: Callable[[tuple[str, int]], None] = lambda x: print(x[0], x[-1])
for item in subject_marks:
    print_grades(item)
