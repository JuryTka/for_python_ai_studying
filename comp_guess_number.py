"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Задачка на проверку алгоритмов
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Изначальная функция
    Взято из задания
    
    Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def random_predict_modified(number:int=1, random_state:bool=False) -> int:
    """Усовершенствованный алгоритм угадывания

    Args:
        number (int, optional):  Передаем число для угадывания. Defaults to 1.
        random_state (bool, optional): Если True генирирует загаданное число. Defaults to False.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    if random_state:
        number = np.random.randint(lower_border, upper_border)

    predicted = False
    # Переменные, ограничивающе область предположения. Сначала от 1 до 100
    lower_border = 1
    upper_border = 101
    
    while not predicted:
        count += 1
                
        predict_number = np.random.randint(lower_border, upper_border) # предполагаемое число
        
        # Если угадали цикл завершится после проверки условной переменной
        if number == predict_number:
            predicted = True
            
        # Если не угадали и предполагаемое число больше - смещаем верхнюю границу до предполагаемого
        # и наоборот
        elif predict_number > number: upper_border = predict_number
        else: lower_border = predict_number
        
    return(count)

def score_game(random_predict) -> int:
    """Взято из задания
        
    За какое количество попыток в среднем из 1000 подходов угадывает оригинальный и
    модифицированный алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    #return(score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)
    score_game(random_predict_modified)