import numpy as np
import json
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Carregando os dados do arquivo JSON
with open('avaliacoes.json', 'r') as file:
    avaliacoes_json = json.load(file)

# Transformando o JSON em uma matriz de dados
filmes = ["Filme1", "Filme2", "Filme3", "Filme4", "Filme5", "Filme6"]
avaliacoes = []
nomes_usuarios = []

for usuario, notas in avaliacoes_json.items():
    nomes_usuarios.append(usuario)
    avaliacoes_usuario = []
    for filme in filmes:
        avaliacoes_usuario.append(notas.get(filme, 0.0))
    avaliacoes.append(avaliacoes_usuario)

avaliacoes = np.array(avaliacoes)

# Normalizando as avaliações
avaliacoes_norm = (avaliacoes - np.mean(avaliacoes, axis=1, keepdims=True)) / np.std(avaliacoes, axis=1, keepdims=True)

# Calculando a similaridade entre Mauro e os outros usuários usando distância Euclidiana
avaliacoes_mauro_norm = avaliacoes_norm[-1]
avaliacoes_mauro = avaliacoes[-1]  # Declarando avaliacoes_mauro para uso posterior

distancias = {}

for i, avaliacoes_usuario_norm in enumerate(avaliacoes_norm[:-1]):
    distancias[nomes_usuarios[i]] = euclidean(avaliacoes_mauro_norm, avaliacoes_usuario_norm)

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

# Gerando gráficos e salvando em um arquivo PDF
pdf_filename = "similaridades_recomendacoes.pdf"

with PdfPages(pdf_filename) as pdf:
    # Gráfico de Similaridades
    plt.figure(figsize=(10, 5))
    plt.bar(similaridades.keys(), similaridades.values(), color='skyblue')
    plt.xlabel('Usuários')
    plt.ylabel('Similaridade')
    plt.title('Similaridade entre Mauro e Outros Usuários')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Gráfico de Pesos dos Filmes
    plt.figure(figsize=(10, 5))
    plt.bar(pesos_filmes.keys(), pesos_filmes.values(), color='lightgreen')
    plt.xlabel('Filmes')
    plt.ylabel('Peso')
    plt.title('Pesos dos Filmes Não Assistidos por Mauro')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

print(f"Os gráficos foram salvos no arquivo {pdf_filename}.")
