import random


def your_choice():
    list_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    number = random.choice(list_number)
    return number


first_window = your_choice()
print(first_window)
if first_window % 2 == 0:
    parameter = first_window // 2
else:
    parameter = (first_window + 1) // 2
second_window = ''
for i in range(1, parameter):
    for j in range(2, first_window):
        if first_window % (i + j) == 0:
            second_window += (str(i) + str(j))
print(second_window)
