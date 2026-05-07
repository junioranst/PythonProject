import random
from colorama import Fore, Style, init

init(autoreset=True)

tamanho = 5
navios = 3

tabuleiro = [["~"] * tamanho for _ in range(tamanho)]
tabuleiro_jogador = [["~"] * tamanho for _ in range(tamanho)]

posicoes_navios = []

for _ in range(navios):
    while True:
        linha = random.randint(0, tamanho-1)
        coluna = random.randint(0, tamanho-1)
        if (linha, coluna) not in posicoes_navios:
            posicoes_navios.append((linha, coluna))
            break


def mostrar_tabuleiro():
    print(Fore.CYAN + "\n   A B C D E")
    for i in range(tamanho):
        print(Fore.YELLOW + str(i+1), end="  ")
        for j in range(tamanho):
            simbolo = tabuleiro_jogador[i][j]

            if simbolo == "X":
                print(Fore.RED + "X", end=" ")
            elif simbolo == "O":
                print(Fore.WHITE + "O", end=" ")
            else:
                print(Fore.BLUE + "~", end=" ")
        print()


def converter_letra(letra):
    letras = ["A","B","C","D","E"]
    return letras.index(letra)


acertos = 0
tentativas = 10

print(Fore.GREEN + "="*40)
print(Fore.GREEN + "        🚢 BATALHA NAVAL 🚢")
print(Fore.GREEN + "="*40)
print("Afunde todos os navios!")
print("Você tem", tentativas, "tentativas.\n")


while tentativas > 0 and acertos < navios:

    mostrar_tabuleiro()

    try:
        coluna = input("\nEscolha a coluna (A-E): ").upper()
        linha = int(input("Escolha a linha (1-5): ")) - 1

        coluna = converter_letra(coluna)

    except:
        print(Fore.RED + "Entrada inválida!")
        continue

    if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
        print(Fore.RED + "Posição fora do tabuleiro!")
        continue

    if tabuleiro_jogador[linha][coluna] != "~":
        print(Fore.YELLOW + "Você já tentou aqui!")
        continue

    if (linha, coluna) in posicoes_navios:
        print(Fore.GREEN + "💥 ACERTOU UM NAVIO!")
        tabuleiro_jogador[linha][coluna] = "X"
        acertos += 1
    else:
        print(Fore.WHITE + "🌊 Água...")
        tabuleiro_jogador[linha][coluna] = "O"

    tentativas -= 1

    print(Fore.MAGENTA + f"\nNavios restantes: {navios - acertos}")
    print(Fore.MAGENTA + f"Tentativas restantes: {tentativas}")

if acertos == navios:
    print(Fore.GREEN + "\n🏆 PARABÉNS! VOCÊ VENCEU!")
else:
    print(Fore.RED + "\n💀 Fim de jogo!")

print(Fore.CYAN + "\nPosições dos navios:")
print(posicoes_navios)