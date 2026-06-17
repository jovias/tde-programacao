import threading
import time


LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def tarefa(nome):
    print("[" + nome + "] tentando pegar LOCK_A")
    LOCK_A.acquire()
    print("[" + nome + "] pegou LOCK_A")

    time.sleep(0.3)

    print("[" + nome + "] tentando pegar LOCK_B")
    LOCK_B.acquire()
    print("[" + nome + "] pegou LOCK_B")

    print("[" + nome + "] executando secao critica")
    time.sleep(0.2)

    LOCK_B.release()
    print("[" + nome + "] liberou LOCK_B")

    LOCK_A.release()
    print("[" + nome + "] liberou LOCK_A")

    print("[" + nome + "] terminou")


def main():
    print("\n--- Execucao da versao corrigida ---")

    t1 = threading.Thread(target=tarefa, args=("Thread 1",), name="T1-corrigida")
    t2 = threading.Thread(target=tarefa, args=("Thread 2",), name="T2-corrigida")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Todos terminaram sem deadlock.")


if __name__ == "__main__":
    main()
