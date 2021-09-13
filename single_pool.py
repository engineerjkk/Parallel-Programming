
import time, os

def work_func(x):
    print("value %s is in PID : %s" % (x, os.getpid()))
    time.sleep(1)
    return x**5

def main():
    start = int(time.time())
    print(list(map(work_func, range(0,12))))
    print("***run time(sec) :", int(time.time()) - start)

if __name__ == "__main__":
    main()

#결과를 보면 1개의 피드(PID : 12448)가 작업을 처리하고, 1초간 멈추라고 했으므로 작업 수행까지 12초가 걸린 것을 확인 할 수 있다.