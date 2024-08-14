import numpy as np
from scipy.spatial.distance import euclidean

# Definindo a matriz de dados
avaliacoes = np.array([
    [3.0, 3.5, 1.5, 5.0, 3.0, 3.5],   # Paulo
    [2.5, 3.0, 0.0, 3.5, 0.0, 4.0],   # João
    [0.0, 3.5, 3.0, 4.0, 2.5, 4.5],   # Márcia
    [3.0, 4.0, 0.0, 5.0, 3.5, 3.0],   # Carlos
    [2.5, 3.5, 3.0, 3.5, 2.5, 3.0],   # Ana
    [0.0, 4.0, 0.0, 4.0, 1.0, 0.0]    # Mauro
])

# Nome dos usuários
nomes_usuarios = ['Paulo', 'João', 'Márcia', 'Carlos', 'Ana', 'Mauro']

# Calculando a similaridade entre Mauro e os outros usuários usando distância Euclidiana
avaliacoes_mauro = avaliacoes[-1]
distancias = {}

for i, avaliacoes_usuario in enumerate(avaliacoes[:-1]):
    distancias[nomes_usuarios[i]] = euclidean(avaliacoes_mauro, avaliacoes_usuario)

# Exibindo as distâncias
print("Distâncias Euclidianas:")
for usuario, distancia in distancias.items():
    print(f"{usuario}: {distancia:.2f}")

# Calculando a similaridade usando a distância Euclidiana
similaridades = {usuario: 1 / (1 + distancia) for usuario, distancia in distancias.items()}

# Exibindo as similaridades
print("\nSimilaridades:")
for usuario, similaridade in similaridades.items():
    print(f"{usuario}: {similaridade:.4f}")

# Passo 2 - Calcular o peso dos filmes não assistidos por Mauro
# Para definição do peso, vamos fazer o somatório ponderado das notas do filme
# multiplicado pela similaridade do usuário e dividir pela soma das similaridades.

pesos_filmes = {}
for indice_filme in range(avaliacoes.shape[1]):
    if avaliacoes_mauro[indice_filme] == 0.0:  # Filmes não assistidos por Mauro
        soma_ponderada = sum(avaliacoes[indice_usuario, indice_filme] * similaridades[nomes_usuarios[indice_usuario]] for indice_usuario in range(avaliacoes.shape[0] - 1))
        soma_similaridades = sum(similaridades[nomes_usuarios[indice_usuario]] for indice_usuario in range(avaliacoes.shape[0] - 1))
        pesos_filmes[f"Filme {indice_filme + 1}"] = soma_ponderada / soma_similaridades

# Exibindo os pesos dos filmes não assistidos por Mauro
print("\nPesos dos filmes não assistidos por Mauro:")
for filme, peso in pesos_filmes.items():
    print(f"{filme}: {peso:.4f}")
