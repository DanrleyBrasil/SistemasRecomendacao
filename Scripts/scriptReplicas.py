import json
import random

# Dados originais (não são usados diretamente para a geração, mas fornecidos como referência)
avaliacoes = {
    "Paulo": {
        "Filme1": 3.0,
        "Filme2": 3.5,
        "Filme3": 1.5,
        "Filme4": 5.0,
        "Filme5": 3.0,
        "Filme6": 3.5
    },
    "João": {
        "Filme1": 2.5,
        "Filme2": 3.0,
        "Filme4": 3.5,
        "Filme6": 4.0
    },
    "Márcia": {
        "Filme2": 3.5,
        "Filme3": 3.0,
        "Filme4": 4.0,
        "Filme5": 2.5,
        "Filme6": 4.5
    },
    "Carlos": {
        "Filme1": 3.0,
        "Filme2": 4.0,
        "Filme4": 5.0,
        "Filme5": 3.5,
        "Filme6": 3.0
    },
    "Ana": {
        "Filme1": 2.5,
        "Filme2": 3.5,
        "Filme3": 3.0,
        "Filme4": 3.5,
        "Filme5": 2.5,
        "Filme6": 3.0
    },
    "Mauro": {
        "Filme2": 4.0,
        "Filme4": 4.0,
        "Filme5": 1.0
    }
}

def gerar_replicas(dados, num_replicas):
    filmes = ["Filme1", "Filme2", "Filme3", "Filme4", "Filme5", "Filme6"]
    
    dados_replicados = {}
    
    for i in range(num_replicas):
        usuario = f"Usuario_{i+1}"
        avaliacoes_usuario = {}
        
        for filme in filmes:
            # Gera uma avaliação aleatória entre 0.0 e 5.0
            avaliacao = round(random.uniform(0.0, 5.0), 1)
            avaliacoes_usuario[filme] = avaliacao
        
        dados_replicados[usuario] = avaliacoes_usuario
    
    return dados_replicados

def salvar_em_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

if __name__ == "__main__":
    num_replicas = int(input("Quantas réplicas você deseja gerar? "))
    dados_replicados = gerar_replicas(avaliacoes, num_replicas)
    salvar_em_json(dados_replicados, 'DATASET.json')
    print("Arquivo JSON gerado com sucesso!")
