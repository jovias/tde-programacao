Nome do grupo e dos integrantes:

- Guilherme Camargo Rocha dos Santos
- Joao Vitor Pereira da Silva

Linguagem escolhida:

- Python

---------------------------------------------------------------------------------------------

Parte 1 - Jantar dos Filosofos (Versao Ingenua)
Responsavel: Joao Vitor Pereira da Silva

Objetivo:

- Fazer a implementacao do jantar dos filosofos usando threads com Python.
- Simular a forma ingenua, em que cada filosofo tenta pegar primeiro o garfo da esquerda e depois o garfo da direita.
- Demonstrar que essa estrategia pode resultar em deadlock.

Implementacao:

- Cada filosofo foi representado por uma thread.
- Cada garfo foi representado por um `threading.Lock()`.
- O ciclo de cada filosofo e: pensar, ficar com fome, tentar pegar os dois garfos, comer, liberar os garfos e voltar a pensar.
- Todos seguem a mesma ordem: primeiro o garfo esquerdo e depois o direito.
- Foi usado `time.sleep(0.05)` entre os `acquire()` para aumentar a chance de todos pegarem o primeiro garfo antes de tentar pegar o segundo.

Por que o deadlock surge:

- O deadlock surge porque todos os filosofos podem pegar o garfo esquerdo ao mesmo tempo.
- Depois disso, cada um fica esperando o garfo direito, que esta com o proximo filosofo.
- Como nenhum filosofo libera o garfo que ja pegou, todos ficam bloqueados.

As 4 condicoes de Coffman:

- Exclusao mutua: cada garfo so pode estar com um filosofo por vez. Isso e garantido pelo `threading.Lock()`.
- Manter e esperar: o filosofo segura o garfo esquerdo enquanto espera o direito.
- Nao preempcao: nenhum filosofo consegue tirar o garfo da mao de outro a forca. O garfo so e liberado com `release()`.
- Espera circular: F0 espera F1, F1 espera F2, F2 espera F3, F3 espera F4 e F4 espera F0.

Pseudocodigo:

```text
para cada filosofo i:
    pensar()
    estado[i] = "com fome"
    adquirir(garfo_esquerdo)
    adquirir(garfo_direito)
    estado[i] = "comendo"
    comer()
    liberar(garfo_direito)
    liberar(garfo_esquerdo)
    estado[i] = "pensando"
```

Print do terminal travado:

![Print da Parte 1](image.png)

Como rodar:

```powershell
python "parte1-filósofos\FilosofosVerIngenua.py"
```

---------------------------------------------------------------------------------------------

Parte 3 - Deadlock com duas threads
Responsavel: Guilherme Camargo Rocha dos Santos

Objetivo:

- Fazer um exemplo simples de deadlock usando threads em Python.
- Usar dois locks, chamados `LOCK_A` e `LOCK_B`.
- Mostrar uma versao que trava e uma versao corrigida.

Implementacao da versao com deadlock:

- Foram criadas duas threads.
- A Thread 1 pega primeiro o `LOCK_A` e depois tenta pegar o `LOCK_B`.
- A Thread 2 pega primeiro o `LOCK_B` e depois tenta pegar o `LOCK_A`.
- Tem um `time.sleep(0.3)` entre os dois `acquire()`, para dar tempo das duas threads pegarem o primeiro lock.
- Depois disso, cada uma fica esperando o lock que esta com a outra.

Por que trava:

- A Thread 1 fica segurando o `LOCK_A` e esperando o `LOCK_B`.
- A Thread 2 fica segurando o `LOCK_B` e esperando o `LOCK_A`.
- Como nenhuma libera o lock que ja pegou, o programa fica parado e nao chega no `Fim`.

As 4 condicoes de Coffman:

- Exclusao mutua: cada lock so pode estar com uma thread por vez.
- Manter e esperar: cada thread segura um lock enquanto espera o outro.
- Nao preempcao: uma thread nao consegue forcar a outra a liberar o lock.
- Espera circular: a Thread 1 espera a Thread 2, e a Thread 2 espera a Thread 1.

Versao corrigida:

- Na versao corrigida, as duas threads seguem a mesma ordem.
- As duas pegam primeiro o `LOCK_A` e depois o `LOCK_B`.
- Assim uma thread pode esperar, mas nao fica segurando `LOCK_B` enquanto espera `LOCK_A`.
- A condicao quebrada foi a espera circular.

Pseudocodigo da versao com deadlock:

```text
Thread 1:
    pega LOCK_A
    espera um pouco
    tenta pegar LOCK_B

Thread 2:
    pega LOCK_B
    espera um pouco
    tenta pegar LOCK_A
```

Pseudocodigo da versao corrigida:

```text
Thread 1:
    pega LOCK_A
    pega LOCK_B
    libera LOCK_B
    libera LOCK_A

Thread 2:
    pega LOCK_A
    pega LOCK_B
    libera LOCK_B
    libera LOCK_A
```

Como rodar:

```powershell
python "parte3\versao_com_deadlock.py"
python "parte3\versao_corrigida.py"
```

Na versao com deadlock, o terminal vai ficar parado. Para sair, use `Ctrl + C`.

Print da versao com deadlock:

![Print do terminal da versao que ocorre deadlock](parte3/log_deadlock.png)

Print da versao corrigida:

![Print do terminal da versao corrigida](parte3/log_corrigido.png)

Prints necessarios para a atividade:

- Print da versao com deadlock mostrando a Thread 1 pegando `LOCK_A`.
- Print da versao com deadlock mostrando a Thread 2 pegando `LOCK_B`.
- Print da versao com deadlock mostrando a Thread 1 tentando pegar `LOCK_B` e a Thread 2 tentando pegar `LOCK_A`.
- Print do terminal parado, mostrando que a versao com deadlock nao finaliza.
- Print da versao corrigida mostrando que as duas threads terminaram sem deadlock.

Conclusao:

- A primeira versao trava porque as threads pegam os locks em ordem contraria.
- A segunda versao funciona porque as duas seguem a mesma ordem: `LOCK_A` e depois `LOCK_B`.

---------------------------------------------------------------------------------------------
