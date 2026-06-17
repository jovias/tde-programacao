import threading
import time

N = 5

def filosofo_ingenuo(i, garfo_esq, garfo_dir, estado):
    nome = "F" + str(i)

    print("[" + nome + "] pensando")
    print("  ID da thread:", threading.get_ident())
    print("  Nome:", threading.current_thread().name)
    time.sleep(0.1)

    print("[" + nome + "] com fome")
    estado[i] = "com fome"

    print("[" + nome + "] aguardando garfo esquerdo")
    garfo_esq.acquire()
    print("[" + nome + "] pegou garfo esquerdo")

    time.sleep(0.05)

    print("[" + nome + "] aguardando garfo direito")
    garfo_dir.acquire()
    print("[" + nome + "] pegou garfo direito")

    estado[i] = "comendo"
    print("[" + nome + "] comendo")
    time.sleep(0.2)

    garfo_dir.release()
    garfo_esq.release()
    estado[i] = "pensando"
    print("[" + nome + "] terminou")


def run_ingenuo():
    print("\n--- Execucao da versao ingenua ---")

    garfos = []
    for _ in range(N):
        garfos.append(threading.Lock())

    estado = ["pensando"] * N

    threads = []
    for i in range(N):
        garfo_esq = garfos[i]
        garfo_dir = garfos[(i + 1) % N]
        t = threading.Thread(
            target=filosofo_ingenuo,
            args=(i, garfo_esq, garfo_dir, estado),
            name=f"F{i}-ingenuo"
        )
        threads.append(t)

    for t in threads:
        inicio = time.perf_counter_ns()
        t.start()
        fim = time.perf_counter_ns()
        tempo_criacao = fim - inicio
        print("Thread criada | ID:", t.ident)
        print("  tempo start(ns):", tempo_criacao)

    for t in threads:
        t.join()

    print("Todos terminaram.")


if __name__ == '__main__':
    run_ingenuo()
    print("Fim.")