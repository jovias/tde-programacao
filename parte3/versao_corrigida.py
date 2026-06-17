import threading
import time


# Dois locks representando dois recursos compartilhados.
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

PAUSA_SEGUNDOS = 0.3


def log(mensagem):
    nome_thread = threading.current_thread().name
    print(f"{nome_thread}: {mensagem}", flush=True)


def tarefa():
    # Correcao: todas as threads pegam os locks na mesma ordem.
    # Isso impede a espera circular.
    log("tentando adquirir LOCK_A")
    with LOCK_A:
        log("adquiriu LOCK_A")

        time.sleep(PAUSA_SEGUNDOS)

        log("tentando adquirir LOCK_B")
        with LOCK_B:
            log("adquiriu LOCK_B")
            log("executando secao critica")
            time.sleep(PAUSA_SEGUNDOS)

        log("liberou LOCK_B")

    log("liberou LOCK_A")
    log("finalizou normalmente")


def main():
    print("=== Versao corrigida ===", flush=True)

    thread_1 = threading.Thread(target=tarefa, name="Thread 1")
    thread_2 = threading.Thread(target=tarefa, name="Thread 2")

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print()
    print("As duas threads terminaram sem deadlock.")


if __name__ == "__main__":
    main()
