import time
from concurrent.futures import ProcessPoolExecutor

def print_num(number):
    time.sleep(1)
    return number * number

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,1,5,4,8]

    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_num, numbers)

        for result in results:
            print(result)

    print("Time taken:", time.time() - t)
