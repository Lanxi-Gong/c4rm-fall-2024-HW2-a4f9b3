import numpy as np
def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    result = np.array(numbers, dtype=object)
    
    result[(numbers % 3 == 0) & (numbers % 5 == 0)] = "fizzbuzz"
    result[numbers % 3 == 0] = "fizz"
    result[numbers % 5 == 0] = "buzz"
    
    return result.tolist()

x = FizzBuzz(40,45)
