import threading
import time


LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def tarefa_1():
    print("[Thread 1] tentando pegar LOCK_A")
    LOCK_A.acquire()
    print("[Thread 1] pegou LOCK_A")

    time.sleep(0.3)

    print("[Thread 1] tentando pegar LOCK_B")
    LOCK_B.acquire() #lock B ja esta foi adquirido pela thread 2, entao a thread 1 fica esperando para adquirir o lock B

    print("[Thread 1] terminou")
    LOCK_B.release()
    LOCK_A.release()


def tarefa_2():
    print("[Thread 2] tentando pegar LOCK_B")
    LOCK_B.acquire()
    print("[Thread 2] pegou LOCK_B")

    time.sleep(0.3)

    print("[Thread 2] tentando pegar LOCK_A")
    LOCK_A.acquire()#lock A ja esta foi adquirido pela thread 1, entao a thread 2 fica esperando para adquirir o lock A
    print("[Thread 2] pegou LOCK_A")

    print("[Thread 2] terminou")
    LOCK_A.release()
    LOCK_B.release()


def main():
    print("\n--- Execucao da versao com deadlock ---")

    t1 = threading.Thread(target=tarefa_1, name="T1-deadlock")
    t2 = threading.Thread(target=tarefa_2, name="T2-deadlock")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Fim.")


if __name__ == "__main__":
    main()
