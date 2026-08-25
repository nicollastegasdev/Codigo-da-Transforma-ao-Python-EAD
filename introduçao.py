from datetime import datetime

# Atividade 2 - Comandos simples
print("Olá, mundo!")

nome_teste = "Python"
idade = 15

print(nome_teste)
print(idade)

print(type(nome_teste))
print(type(idade))

# Atividade 3 - Nome do usuário
nome = input("Digite seu nome: ")

print("Olá, " + nome + "! Seja bem-vindo(a)!")

# Desafio extra - Hora atual
hora = datetime.now().strftime("%H:%M:%S")

print("A hora atual é:", hora)