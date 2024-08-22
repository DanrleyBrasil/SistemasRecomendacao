import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Função para carregar e processar dados do arquivo JSON
def load_ratings_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Obter todos os filmes (colunas) e usuários (linhas)
    filmes = list(next(iter(data.values())).keys())
    usuarios = list(data.keys())
    
    # Criar uma matriz de avaliações
    ratings_matrix = np.zeros((len(usuarios), len(filmes)))
    
    # Preencher a matriz com as avaliações do JSON
    for i, usuario in enumerate(usuarios):
        for j, filme in enumerate(filmes):
            ratings_matrix[i, j] = data[usuario].get(filme, 0.0)
    
    return ratings_matrix, usuarios, filmes

# Carregar dados do arquivo JSON
ratings, usuarios, filmes = load_ratings_from_json('DATASET.json')

# Similaridade entre usuários
user_similarity = cosine_similarity(ratings)

# Recomendar itens para um usuário específico (por exemplo, Mauro, que é o usuário com índice 5)
user_id = 1
user_ratings = ratings[user_id]
similar_users = user_similarity[user_id]

# Inicializar o vetor de pontuação de recomendação
recommendation_scores = np.zeros(ratings.shape[1])

# Calcular a pontuação de recomendação
for item in range(ratings.shape[1]):
    # Inicializar acumuladores de somas de similaridades e pesos
    sum_similarity = 0
    weighted_ratings_sum = 0
    
    for user in range(ratings.shape[0]):
        if user != user_id and ratings[user, item] > 0:  # Considerar apenas avaliações reais
            sum_similarity += similar_users[user]
            weighted_ratings_sum += similar_users[user] * ratings[user, item]
    
    # Evitar divisão por zero
    if sum_similarity > 0:
        recommendation_scores[item] = weighted_ratings_sum / sum_similarity
    else:
        recommendation_scores[item] = 0

# Exibir pontuações de recomendação para o usuário
print("Pontuações de recomendação:", recommendation_scores)

# Exibir recomendações para o usuário
recommended_items = np.argsort(recommendation_scores)[::-1]  # Itens com maior pontuação no início
print("Itens recomendados (baseado na pontuação):")
for item in recommended_items:
    print(f"{filmes[item]} com pontuação {recommendation_scores[item]:.2f}")
