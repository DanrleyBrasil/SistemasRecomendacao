import numpy as np

# Representação dos usuários e filmes
usuarios = {
    "Paulo": np.array([0, 1, 0, 0, 1, 1]),
    "Joao": np.array([1, 1, 0, 0, 0, 0]),
    "Marcia": np.array([0, 0, 1, 1, 1, 0]),
    "Carlos": np.array([0, 0, 1, 0, 0, 0]),
    "Ana": np.array([1, 0, 0, 0, 0, 0]),
    "Mauro": np.array([0, 1, 1, 0, 0, 0])
}

# Vetor de Mauro
mauro = usuarios["Mauro"]

# Função para calcular a similaridade cosseno
def cosine_similarity(user1, user2):
    dot_product = np.dot(user1, user2)
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)
    if norm_user1 == 0 or norm_user2 == 0:  # Evitar divisão por zero
        return 0
    return dot_product / (norm_user1 * norm_user2)

# Calcular similaridade entre Mauro e os outros usuários
similaridades = {}
for nome, vetor in usuarios.items():
    if nome != "Mauro":
        similaridades[nome] = cosine_similarity(mauro, vetor)

# Exibir similaridades
print("Similaridades com Mauro:")
for nome, similaridade in similaridades.items():
    print(f"{nome}: {similaridade:.4f}")

# Ordenar usuários pela similaridade com Mauro
usuarios_similares = sorted(similaridades.items(), key=lambda x: x[1], reverse=True)

print("\nUsuários mais similares a Mauro:")
for nome, similaridade in usuarios_similares:
    print(f"{nome}: {similaridade:.4f}")

# Recomendar filmes para Mauro
def recomendar_filmes(usuario_alvo, usuarios_similares, usuarios, n_recomendacoes=3):
    recomendacoes = np.zeros(len(usuario_alvo))
    for nome, _ in usuarios_similares:
        recomendacoes += usuarios[nome]
    
    recomendacoes = np.where(usuario_alvo == 0, recomendacoes, 0)  # Considerar apenas filmes que Mauro não assistiu
    filmes_recomendados = np.argsort(recomendacoes)[::-1][:n_recomendacoes]  # Pegar os índices dos filmes mais recomendados
    
    return filmes_recomendados

# Obter recomendações
filmes_recomendados = recomendar_filmes(mauro, usuarios_similares, usuarios)
print("\nFilmes recomendados para Mauro:")
print(filmes_recomendados)
