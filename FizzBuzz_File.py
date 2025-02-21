import numpy as np
def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    result = np.array(numbers, dtype=object)
    
    result[(numbers % 3 == 0) & (numbers % 5 != 0)] = 'Fizz'
    result[(numbers % 5 == 0) & (numbers % 3 != 0)] = 'Buzz'
    result[(numbers % 3 == 0) & (numbers % 5 == 0)] = 'FizzBuzz'
    
    return result.tolist()

x = FizzBuzz(40,45)
