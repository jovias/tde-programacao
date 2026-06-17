import threading
import time


# Dois locks representando dois recursos compartilhados.
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

# A pausa ajuda as duas threads a pegarem o primeiro lock
# antes de tentarem pegar o segundo.
PAUSA_SEGUNDOS = 0.3


def log(mensagem):
    nome_thread = threading.current_thread().name
    print(f"{nome_thread}: {mensagem}", flush=True)


def tarefa_1():
    log("tentando adquirir LOCK_A")
    LOCK_A.acquire()
    log("adquiriu LOCK_A")

    time.sleep(PAUSA_SEGUNDOS)

    log("tentando adquirir LOCK_B")
    LOCK_B.acquire()

    # Em deadlock, normalmente o codigo abaixo nao executa.
    log("adquiriu LOCK_B")
    LOCK_B.release()
    LOCK_A.release()


def tarefa_2():
    log("tentando adquirir LOCK_B")
    LOCK_B.acquire()
    log("adquiriu LOCK_B")

    time.sleep(PAUSA_SEGUNDOS)

    log("tentando adquirir LOCK_A")
    LOCK_A.acquire()

    # Em deadlock, normalmente o codigo abaixo nao executa.
    log("adquiriu LOCK_A")
    LOCK_A.release()
    LOCK_B.release()


def main():
    print("=== Versao com deadlock ===", flush=True)

    # daemon=True permite que o programa encerre depois da deteccao,
    # mesmo com as threads travadas esperando os locks.
    thread_1 = threading.Thread(target=tarefa_1, name="Thread 1", daemon=True)
    thread_2 = threading.Thread(target=tarefa_2, name="Thread 2", daemon=True)

    thread_1.start()
    thread_2.start()

    thread_1.join(timeout=2)
    thread_2.join(timeout=2)

    if thread_1.is_alive() and thread_2.is_alive():
        print()
        print("Deadlock detectado.")
        print("Thread 1 segura LOCK_A e espera LOCK_B.")
        print("Thread 2 segura LOCK_B e espera LOCK_A.")
        print("O programa nao consegue finalizar normalmente nessa situacao.")


if __name__ == "__main__":
    main()
