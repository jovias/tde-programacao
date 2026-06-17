import threading
import time

N = 5

def filosofo_corrigido(i, garfos, estado):
    nome = "F" + str(i)

    # Hierarquia de recursos: sempre adquire o garfo de menor índice primeiro
    esq = i
    dir = (i + 1) % N
    primeiro = min(esq, dir)
    segundo = max(esq, dir)

    print("[" + nome + "] pensando")
    print("  ID da thread:", threading.get_ident())
    print("  Nome:", threading.current_thread().name)
    time.sleep(0.1)

    print("[" + nome + "] com fome")
    estado[i] = "com fome"

    print("[" + nome + "] aguardando garfo " + str(primeiro) + " (menor índice)")
    garfos[primeiro].acquire()
    print("[" + nome + "] pegou garfo " + str(primeiro))

    time.sleep(0.05)

    print("[" + nome + "] aguardando garfo " + str(segundo) + " (maior índice)")
    garfos[segundo].acquire()
    print("[" + nome + "] pegou garfo " + str(segundo))

    estado[i] = "comendo"
    print("[" + nome + "] comendo")
    time.sleep(0.2)

    garfos[segundo].release()
    print("[" + nome + "] liberou garfo " + str(segundo))
    garfos[primeiro].release()
    print("[" + nome + "] liberou garfo " + str(primeiro))

    estado[i] = "pensando"
    print("[" + nome + "] terminou")

def run_corrigido():
    print("\n--- Execucao da versao corrigida (hierarquia de recursos) ---")

    garfos = []
    for _ in range(N):
        garfos.append(threading.Lock())

    estado = ["pensando"] * N

    threads = []
    for i in range(N):
        t = threading.Thread(
            target=filosofo_corrigido,
            args=(i, garfos, estado),
            name=f"F{i}-corrigido"
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

    print("Todos terminaram sem deadlock.")

if __name__ == '__main__':
    run_corrigido()
    print("Fim.")