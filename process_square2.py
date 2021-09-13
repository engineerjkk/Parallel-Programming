import os
import time

from multiprocessing import Process, current_process


def cube(numbers):
    for number in numbers:
        time.sleep(0.5)
        print(f"The number {number} cubes to {number*number*number}.")


def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        print(f"The number {number} squares to {number*number}.")


if __name__ == '__main__':

    processes = []
    numbers = range(100)

    for i in range(100):
        process = Process(target=square, args=(numbers,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# 주석 삭제후 테스트 가능
    #p1 = Process(target=square, args=(numbers,))
    #p2 = Process(target=cube, args=(numbers,))
    #p3 = Process(target=square, args=(numbers,))

    #p1.start()
    #p2.start()
    #p3.start()

    #p1.join()
    #p2.join()
    #p3.join()

    print("Multiprocessing process complete")