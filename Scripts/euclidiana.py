import json
from math import sqrt

# Função para carregar dados do arquivo JSON
def load_ratings_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Função para calcular a distância euclidiana entre dois usuários
def dist_euclidiana(usuario1, usuario2):
    sim = {}
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            sim[item] = 1

    if len(sim) == 0:
        return 0

    distancia = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
                     for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])

    # Similaridade
    return 1 / (1 + sqrt(distancia))

# Função para calcular similaridades entre usuários
def calc_similaridades(alvo):
    similaridades = [(dist_euclidiana(alvo, usuario2), usuario2) for usuario2 in avaliacoes if usuario2 != alvo]
    return similaridades

# Função para calcular recomendações para um usuário específico
def calc_recomendacoes(alvo):
    totais = {}
    soma_sim = {}
    for usuario2 in avaliacoes:
        if usuario2 == alvo: continue
        similaridade = dist_euclidiana(alvo, usuario2)

        if similaridade <= 0: continue

        for item in avaliacoes[usuario2]:
            if item not in avaliacoes[alvo]:
                totais.setdefault(item, 0)
                totais[item] += avaliacoes[usuario2][item] * similaridade
                soma_sim.setdefault(item, 0)
                soma_sim[item] += similaridade

    ranking = [(total / soma_sim[item], item) for item, total in totais.items()]
    ranking.sort()
    ranking.reverse()
    
    return ranking

# Carregar os dados do arquivo JSON
avaliacoes = load_ratings_from_json('old_dataset.json')

# Exemplos de uso
usuario = 'Mauro'  # Substitua pelo usuário para o qual deseja fazer recomendações
print("Similaridades para", usuario)
print(calc_similaridades(usuario))

print("\nRecomendações para", usuario)
print(calc_recomendacoes(usuario))
