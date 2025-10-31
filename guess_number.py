"""Угадываем число самостоятельно
"""

import numpy as np


def guess_number():
    number = np.random.randint(1, 101) # загадываем число
    count = 0

    while True:
        count += 1
        predict_number = int(input("Угадай число от 1 до 100\n"))

        if predict_number > number:
            print("Число должно быть меньше!\n")

        elif predict_number < number:
            print("Число должно быть больше!\n")

        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток\n")
            break # конец игры, выход из цикла
    return