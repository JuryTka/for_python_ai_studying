import numpy as np

def random_predict(number: int = 1) -> int:
    count = 0
    
    #if number != 1:
    #    number = np.random.randint(1, 100)
    
    predicted = False
    while not predicted:
        count += 1
        predict_number = np.random.randint(1, 100)
        if predict_number == number:
            predicted = True
    return count



num = np.random.randint(1, 100)
print(f" {random_predict(num)} " )