import random
import math

numero_secreto = random.randint(1, 100)

print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente adivinhar um número entre 1 e 100!")

tentativa = int(input("Digite sua tentativa: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
elif tentativa < numero_secreto:
    print("O número secreto é maior!")
    print("A diferença é de:", math.fabs(numero_secreto - tentativa))
else:
    print("O número secreto é menor!")
    print("A diferença é de:", math.fabs(numero_secreto - tentativa))

print("O número secreto era:", numero_secreto)