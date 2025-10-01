import multiprocessing
import sys
import time 
import math

sys.set_int_max_str_digits(100000)


def computer_factorial(number):
    print(f"computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[500]

    start_time= time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)

    end_time = time.time() - start_time


    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
