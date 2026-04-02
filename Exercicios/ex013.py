from datetime import datetime
hoje = datetime.today()
print(f'Data de hoje {hoje.strftime('%d/%m/%Y')}')

nascimento = input('Digite o seu ano de nascimento em formato dd/mm/aaaa: ')
nascimento = datetime.strptime(nascimento, '%d/%m/%Y')

idade = (hoje.year - nascimento.year)

if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -=1

if idade < 18:
    print(f'voce ainda nao tem idade para se alistar, {idade} anos de idade')
elif idade == 18:
    print(f'voce esta no ano de alistamento, {idade} anos de idade')
elif idade > 18:
    print(f'Já passou do prazo de alistamento, {idade} anos de idade')


