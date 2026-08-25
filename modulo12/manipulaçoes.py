import json

clientes = {
    "cliente1": {
        "nome": "João",
        "idade": 20,
        "cidade": "São Paulo"
    },
    "cliente2": {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Rio de Janeiro"
    }
}

# Salvando os dados no arquivo JSON
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

# Carregando os dados do arquivo JSON
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    clientes_carregados = json.load(arquivo)

print("Clientes:")
print(clientes_carregados)