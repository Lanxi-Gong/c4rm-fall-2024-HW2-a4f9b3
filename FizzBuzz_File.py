import numpy as np
def FizzBuzz(start, finish):
    numvec = np.arange(start, finish+1)
    objvec = np.array(numvec, dtype=object)

    objvec[(numvec % 3 == 0) & (numvec % 5 != 0)] = 'Fizz'
    objvec[(numvec % 5 == 0) & (numvec % 3 != 0)] = 'Buzz'
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = 'FizzBuzz'

    return objvec

start = 40
finish = 45

result = FizzBuzz(start, finish)
print(result)
