# Importa duas funções do módulo 'time':
# 'sleep' serve para pausar a execução por alguns segundos.
# 'time' serve para marcar o tempo atual (timestamp).
from time import sleep, time  

# Marca o tempo de início da execução do programa (usado para medir o tempo total).
start = time()

# Lista representando os garfos disponíveis (um para cada filósofo).
garfos = [1, 2, 3, 4, 5]

# Lista com os nomes dos filósofos.
filosofos = ["Sócrates", "Platão", "Parmênides", "Aristóteles", "Maquiavel"]

# Lista que armazenará os nomes dos filósofos que conseguiram comer.
filosofos_que_comeram = []

# Lista que manterá o controle dos garfos que estão em uso no momento.
garfos_em_uso = []

# Função que representa o ato de um filósofo comer.
def comer(filosofo, garfo_esquerdo, garfo_direito):
    # Mostra que o filósofo pegou os dois garfos (esquerdo e direito).
    print(f"Filósofo {filosofo} pegou os garfos {garfo_esquerdo} e {garfo_direito}")
    
    # Pausa por 1.5 segundos para simular o tempo que o filósofo está comendo.
    sleep(1.5)
    
    # Indica que o filósofo terminou de comer e vai liberar os garfos.
    print(f"{filosofo} terminou de comer e liberou os garfos")
    
    # Adiciona o filósofo à lista dos que comeram.
    filosofos_que_comeram.append(filosofo)

# Loop que percorre a lista de filósofos.
for i, filosofo in enumerate(filosofos):
    # Define o garfo à esquerda do filósofo (baseado no índice).
    garfo_esquerdo = garfos[i]
    
    # Define o garfo à direita (o próximo da lista, com rotação circular usando módulo).
    garfo_direito = garfos[(i + 1) % len(garfos)]

    # Verifica se ambos os garfos necessários não estão em uso.
    if garfo_esquerdo not in garfos_em_uso and garfo_direito not in garfos_em_uso:
        # Adiciona os dois garfos à lista de garfos em uso.
        garfos_em_uso.extend([garfo_esquerdo, garfo_direito])
        
        # Chama a função para o filósofo comer com os garfos disponíveis.
        comer(filosofo, garfo_esquerdo, garfo_direito)
        
        # Após comer, remove os garfos da lista de garfos em uso.
        garfos_em_uso.remove(garfo_esquerdo)
        garfos_em_uso.remove(garfo_direito)
    else:
        # Caso algum garfo esteja ocupado, o filósofo não pode comer agora.
        print(f"{filosofo} está pensando, (garfos_ocupados)")

# Imprime a lista dos filósofos que conseguiram comer.
print(f"'Filósofos que comeram: {filosofos_que_comeram}")

# Marca o tempo de término da execução.
end = time()

# Calcula a duração total da execução do programa.
length = end - start

# Imprime o tempo total de execução.
print(length)
