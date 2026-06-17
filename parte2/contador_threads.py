import threading
import time

T = 8
M = 200000
count = 0
sem = threading.Semaphore(1)


def tarefa_sem_sync():
    global count
    for i in range(M):
        count = count + 1


def tarefa_com_sync():
    global count
    for i in range(M):
        sem.acquire()
        try:
            count = count + 1
        finally:
            sem.release()


def executar_versao(funcao, nome):
    global count
    count = 0

    threads = []
    inicio = time.time()

    for i in range(T):
        t = threading.Thread(target=funcao)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fim = time.time()

    print(f"\n--- {nome} ---")
    print(f"Esperado: {T * M}")
    print(f"Obtido:   {count}")
    print(f"Tempo:    {fim - inicio:.2f} segundos")


if __name__ == "__main__":
    executar_versao(tarefa_sem_sync, "SEM sincronizacao")
    executar_versao(tarefa_com_sync, "COM semaforo")