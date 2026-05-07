print('MÉDIA DE NOTAS DOS ALUNOS')
# Titulo do programa

notas = []
# lista onde será colocada as notas

while True:
    entrada = input('Digite a nota da prova (ou "fim" para encerrar): ')
    # Loop para o usuário digitar quantas notas for necessário

    if entrada.lower() == 'fim':
        print('Programa encerrado')
        break
    # caso o usuário digitar fim ou FIM o programa encerra no break
    # Uma mensagem aparecerá na tela informando o encerramento do programa

    else:
        nota = float(entrada)
        # Esta sendo atribuido o valor de float a variavel nota
        notas.append(nota)
# O valor da variavel nota está sendo atribuido a lista notas

if len(notas) > 0:
    # O codico sera continuado apenas se o valor atribuido a lista de notas for
    # for maior que 0, para que nao haja erro ao se digitar FIM

    media_notas = sum(notas) / len(notas)
    # O calulo da media será a soma dos valores da lista (notas) dividido pela
    # quantidade de valoreas atribuido a notas (tamanho da lista)
    print(f'Suas notas foram: {notas}')
    # Será exibido as notas inseridas

    if media_notas >= 7:
        print('Aprovado')
        print(f'Parabéns sua media foi igual a {media_notas:.2f}')
    # Caso a media for maior ou igual a 7 será exibido a nota e a situaçao como Aprovado

    else:
        print('Reprovado')
        print(f'Infelizmente sua media foi igual a {media_notas:.2f}')
# Caso a media for menor que 7 será exibido a nota e a situaçao como Reprovado

