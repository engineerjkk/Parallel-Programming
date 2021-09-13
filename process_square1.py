#square 연산 예제를 통해 각각의 PID 와 square값을 출력한다.
#위 코드를 실행한 결과를 살펴보면 각 실행마다 다른 프로세스(PID가 각각 다름)에서 실행된것을 알 수 있다.

import os

from multiprocessing import Process, current_process


def square(number):
    result = number * number

    # OS 모듈을 통해 PID 저장 및 출력
    proc_id = os.getpid()
    print(f"Process ID: {proc_id}")

    #현재 프로세스 이름
    process_name = current_process().name
    print(f"Process Name: {process_name}")

    print(f"The number {number} squares to {result}.")


if __name__ == '__main__':

    processes = []
    numbers = [1, 2, 3, 4, 5] #list number

    for i, number in enumerate(numbers): #튜플이므로 enumerate 사용
        #Process를 활용해서 function을 호출한다. 우리가 사용할 target 함수는 square이며, arguments는 number이다.
        process = Process(target=square, args=(number,))
        processes.append(process)

        #프로세스는 프로세스 개체를 만든 후에 start() 메서드를 호출하여 생성.
        process.start()

    #process가 끝날 때까지 기다린 후 다음 프로세스를 시작하도록 설정.
    #.join()을 사용해서 프로세스 종료
    for process in processes:

        process.join()