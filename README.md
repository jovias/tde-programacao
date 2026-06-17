Nome do grupo e dos integrantes:

-João Vitor Pereira da Silva

Linguagem escolhida:

-Python

Parte 1 — Jantar dos Filósofos (Versão Ingênua) Responsável: João Vitor Pereira da Silva

Objetivo:

- Fazer a implementação dos jantar dos filósofos usando threads com python, simulando a forma ingênua (cada filósofo tenta pegar primeiro o garfo da esquerda e depois o da direita), nisso resultando em deadlock.

Implementação: 

- Cada filósofo foi representado por uma thread.

- O ciclo de cada filósofo é: 1- pensar, 2- ficar com fome, 3- tentar pegar os dois garfos, 4- comer, 5- liberar os garfos 6- voltar a pensar.

- Todos seguem a mesma ordem (primeiro o garfo esquerdo e depois o direito).

Por que o deadlock surge:

- Porque todos os filósofos seguem a mesma ordem. Aí, por conta do time.sleep(0.05) entre os acquires, aumenta a chance disso acontecer, porque da tempo de todos pegarem o garfo esquerdo antes de qualquer um tirar o direito

As 4 condições de Coffman:

-Exclusão mútua: Cada só pode estar na mão de um filósofo por vez. Isso é garantido pelo threading.Lock(), se um filósofo pegou, o outro fica bloqueado no acquire().

-Manter-e-esperar: O filósofo segura o garfo esquerdo enquanto espera o direito. Ele não larga o que já tem para tentar depois, fica travado segurando um e esperando o outro.

-Não preempção: Nenhum filósofo consegue tirar o garfo da mão do outro à força. O único jeito de liberar um garfo é o próprio filósofo chamar o release() voluntariamente.

-Espera circular: F0 espera F1, F1 espera F2, F2 espera F3, F3 espera F4, F4 espera F0. Forma um ciclo fechado onde ninguém consegue avançar.

Print do terminal Travado:

![alt text](image.png)

