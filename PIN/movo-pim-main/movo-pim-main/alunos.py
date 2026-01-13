import json
import os

ARQUIVO_DADOS = "alunos.json"

def carregar_alunos():
    """Carrega a lista de alunos do arquivo JSON. Retorna uma lista vazia se o arquivo não existir."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se o arquivo estiver corrompido ou vazio, retorna uma lista vazia e imprime um erro
        print(f"Erro: O arquivo '{ARQUIVO_DADOS}' está corrompido ou vazio.")
        return []
    except Exception as e:
        print(f"Erro ao carregar dados dos alunos: {e}")
        return []

def salvar_alunos(lista_alunos):
    """Salva a lista de alunos no arquivo JSON."""
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(lista_alunos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar dados dos alunos: {e}")

# Exemplo de uso (opcional, pode ser removido se você já tiver o seu)
if __name__ == "__main__":
    lista_exemplo = carregar_alunos()
    if not lista_exemplo:
        print("Criando arquivo de exemplo...")
        lista_exemplo = [
            {"RA": "1234", "nome": "Maria Silva", "habilitado": True, "NP1": 7.0, "NP2": 8.5, "PIM": 9.0, "Media": 8.17, "Situacao": "Aprovado"},
            {"RA": "5678", "nome": "João Souza", "habilitado": True, "NP1": 4.5, "NP2": 5.0, "PIM": None, "Media": None, "Situacao": None},
        ]
        salvar_alunos(lista_exemplo)
        print("Arquivo alunos.json criado com sucesso!")
    else:
        print(f"Total de alunos carregados: {len(lista_exemplo)}")