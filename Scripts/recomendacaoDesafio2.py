import numpy as np

# Representação dos usuários e suas avaliações de filmes
usuarios = {
    "Paulo": np.array([3.0, 3.5, 1.5, 5.0, 3.0, 3.5]),
    "Joao": np.array([2.5, 3.0, 0.0, 3.5, 0.0, 4.0]),
    "Marcia": np.array([0.0, 3.5, 3.0, 4.0, 2.5, 4.5]),
    "Carlos": np.array([3.0, 4.0, 0.0, 5.0, 3.5, 3.0]),
    "Ana": np.array([2.5, 3.5, 3.0, 3.5, 2.5, 3.0]),
    "Mauro": np.array([0.0, 4.0, 0.0, 4.0, 1.0, 0.0])
}

# Vetor de avaliações do usuário Mauro
mauro = usuarios["Mauro"]

# Função para calcular a similaridade cosseno entre dois usuários
def cosine_similarity(user1, user2):
    # Produto escalar entre os vetores dos usuários
    dot_product = np.dot(user1, user2)
    # Norma (magnitude) dos vetores dos usuários
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)
    # Verificação para evitar divisão por zero
    if norm_user1 == 0 or norm_user2 == 0:
        return 0
    # Cálculo da similaridade cosseno
    return dot_product / (norm_user1 * norm_user2)

# Dicionário para armazenar as similaridades entre Mauro e os outros usuários
similaridades = {}
for nome, vetor in usuarios.items():
    if nome != "Mauro":
        # Calcula a similaridade cosseno entre Mauro e outro usuário
        similaridades[nome] = cosine_similarity(mauro, vetor)

# Exibe as similaridades calculadas
print("Similaridades com Mauro:")
for nome, similaridade in similaridades.items():
    print(f"{nome}: {similaridade:.4f}")

# Ordena os usuários pela similaridade em relação a Mauro, em ordem decrescente
usuarios_similares = sorted(similaridades.items(), key=lambda x: x[1], reverse=True)

print("\nUsuários mais similares a Mauro:")
for nome, similaridade in usuarios_similares:
    print(f"{nome}: {similaridade:.4f}")

# Função para recomendar filmes a um usuário-alvo com base nas avaliações de usuários similares
def recomendar_filmes(usuario_alvo, usuarios_similares, usuarios, n_recomendacoes=3):
    # Inicializa um vetor de recomendações com zeros
    recomendacoes = np.zeros(len(usuario_alvo))
    # Soma as avaliações dos filmes dos usuários similares
    for nome, _ in usuarios_similares:
        recomendacoes += usuarios[nome]
    
    # Considera apenas os filmes que Mauro não assistiu (onde a avaliação é zero)
    recomendacoes = np.where(usuario_alvo == 0, recomendacoes, 0)
    # Ordena os filmes por ordem de recomendação e seleciona os top N recomendados
    filmes_recomendados = np.argsort(recomendacoes)[::-1][:n_recomendacoes]
    
    return filmes_recomendados

# Obtém as recomendações de filmes para Mauro
filmes_recomendados = recomendar_filmes(mauro, usuarios_similares, usuarios)

print("\nFilmes recomendados para Mauro:")
print(filmes_recomendados)
