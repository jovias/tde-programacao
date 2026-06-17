import threading
import time

NUM_THREADS = 8
NUM_ITERACOES = 200000
contador = 0
sem = threading.Semaphore(1)


def tarefa_sem_sincronizacao():
    global contador
    for i in range(NUM_ITERACOES):
        contador = contador + 1


def tarefa_com_sincronizacao():
    global contador
    for i in range(NUM_ITERACOES):
        sem.acquire()
        try:
            contador = contador + 1
        finally:
            sem.release()


def executar_versao(funcao, nome):
    global contador        
    contador = 0           

    threads = []           
    inicio = time.time()  

    for i in range(NUM_THREADS):  
        t = threading.Thread(target=funcao)  
        threads.append(t)                    
        t.start()                            

    for t in threads:      
        t.join()           

    fim = time.time()      


    print(f"\n--- {nome} ---")    
    print(f"Esperado: {NUM_THREADS * NUM_ITERACOES}")
    print(f"Obtido:   {contador}")
    print(f"Tempo:    {fim - inicio:.2f} segundos")


if __name__ == "__main__":
    executar_versao(tarefa_sem_sincronizacao, "Sem Sincronização")
    executar_versao(tarefa_com_sincronizacao, "Com Semáforo")

