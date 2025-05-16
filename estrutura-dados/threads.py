import threading  # Módulo para trabalhar com threads
from time import sleep, time

# Lista com nomes dos filósofos
filosofos = ["Sócrates", "Platão", "Parmênides", "Aristóteles", "Maquiavel"]

# Criamos um garfo (lock) para cada posição na mesa
# Cada filósofo compartilha o garfo da esquerda com o da direita
garfos = [threading.Lock() for _ in range(5)]

# Lista para guardar os filósofos que conseguiram comer (com sincronização)
filosofos_que_comeram = []

# Lock para acessar/modificar a lista de filósofos_que_comeram
mutex_comida = threading.Lock()

# Função que será executada por cada thread (filósofo)
def jantar(filosofo_index):
    filosofo = filosofos[filosofo_index]
    garfo_esquerdo = garfos[filosofo_index]
    garfo_direito = garfos[(filosofo_index + 1) % 5]

    # Tentamos pegar os garfos, sempre pegando o de menor índice primeiro para evitar deadlock
    primeiro_garfo = garfo_esquerdo if filosofo_index < (filosofo_index + 1) % 5 else garfo_direito
    segundo_garfo = garfo_direito if primeiro_garfo == garfo_esquerdo else garfo_esquerdo

    with primeiro_garfo:  # Pegou o primeiro garfo
        with segundo_garfo:  # Pegou o segundo garfo
            print(f"{filosofo} pegou os dois garfos e está comendo.")
            sleep(1)  # Simula o tempo que está comendo
            print(f"{filosofo} terminou de comer e liberou os garfos.")
            # Atualiza a lista compartilhada de forma segura
            with mutex_comida:
                filosofos_que_comeram.append(filosofo)

# Marca o início da execução
start = time()

# Criamos uma thread para cada filósofo
threads = []

for i in range(5):
    thread = threading.Thread(target=jantar, args=(i,))
    threads.append(thread)
    thread.start()  # Inicia a execução da thread

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

# Exibe o resultado final
print(f"\nFilósofos que comeram: {filosofos_que_comeram}")
end = time()
print(f"Tempo total: {end - start:.2f} segundos")
