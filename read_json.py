import json


def read_json(path):
    try:
            f = open(path, "r", encoding="utf-8")
            content = f.read().strip()
            f.close()
    except FileNotFoundError:
        print("Erro: Ficheiro Não Encontrado!")
        return
    if not path.endswith(".json"):
         print("Erro: Ficheiro Não Contém JSON Válido!")
         return 
    if content == "":
        print("Erro: Ficheiro Vazio!")
        return

    required = ["nome", "idade", "localização"]
    if not all(field in content for field in required):
        print("Erro: Campos Obrigatórios em Falta!")
        return

    print(content)


if __name__ == "__main__":
    file_path = input("")
    read_json(file_path)
    print("Processo Concluído!")

