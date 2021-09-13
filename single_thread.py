from threading import Thread
import time, os

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return


if __name__ == "__main__":
    start = int(time.time())
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=work, args=(1, START, END, result))

    th1.start()
    th1.join()

print(f"Result: {sum(result)}")
print("***run time(sec) :", int(time.time()) - start)