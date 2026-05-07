#=======================================================================================================================
#Classe e Biblioteca
#=======================================================================================================================
class clinica:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __repr__(self):
        return f'\nNome: {self.nome} \nIdade: {self.idade} \nTelefone: {self.telefone}'

biblioteca = []

#=======================================================================================================================
#Funçao para cadastro
#=======================================================================================================================

def cadastro():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    telefone = input('Telefone: ')
    biblioteca.append(clinica(nome, idade, telefone))
    print('O cadastro foi efetuado com sucesso!')

#=======================================================================================================================
#Funçao para buscar paciente pelo nome
#=======================================================================================================================

def lista_pacientes():
    for clinica in biblioteca:
        print(clinica)

#=======================================================================================================================
#Funçao para as estatisticas
#=======================================================================================================================

def estatisticas():
    if len(biblioteca) > 0:

        #numero de pacientes
        print(f'Numero de pacientes cadastrados: {len(biblioteca)}')

        #idade media dos pacientes
        soma_idades = sum(paciente.idade for paciente in biblioteca)
        media = soma_idades / len(biblioteca)
        print(f'A média de idade dos pacientes é de: {media:.2f} anos.')

        #paciente mais novo e mais velho
        mais_velho = max(biblioteca, key=lambda p: p.idade)
        mais_novo = min(biblioteca, key=lambda p: p.idade)
        print(f'Paciente mais velho: {mais_velho.nome} ({mais_velho.idade} anos)')
        print(f'Paciente mais novo: {mais_novo.nome} ({mais_novo.idade} anos)\n')

    else:
        print('Nenhum paciente foi encontrado!')


#=======================================================================================================================
#Funçao para a busca de paciente
#=======================================================================================================================

def buscar_paciente():
    nome_busca = input('Digite o nome do paciente: ').lower()

    encontrados = [p for p in biblioteca if p.nome.lower() == nome_busca]

    if len(encontrados) == 0:
        print('\n Paciente não encontrado!\n')
    else:
        print('\n=== PACIENTE ENCONTRADO ===')
        for p in encontrados:
            print(p)
        print()

#=======================================================================================================================
#Menu Principal
#=======================================================================================================================
while True:
    print('\n=== SISTEMA CLÍNICA VIDA+ ===\n')
    print('1. Cadastrar paciente')
    print('2. Ver estatísticas')
    print('3. Buscar paciente')
    print('4. Listar todos os pacientes')
    print('5. Sair')
    escolha = int(input('\nEscolha uma opção: '))


    if escolha == 1:
        cadastro()

    elif escolha == 2:
        estatisticas()

    elif escolha == 3:
        buscar_paciente()

    elif escolha == 4:
        lista_pacientes()

    elif escolha == 5:
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida!\n')







