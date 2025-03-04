import random

print("🎮 Jogo da Adivinhação 🎮")
print("Adivinhe o número entre 1 e 100!")
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número MAIOR!")
        elif palpite > numero_secreto:
            print("Tente um número MENOR!")
        else:
            print(f"🏆 Parabéns! Você acertou em {tentativas} tentativas!")
            break
    except ValueError:
        print("Por favor, digite apenas números!")

input("Pressione Enter para sair...")
