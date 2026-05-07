from rich import inspect

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade +=1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.curso}, {self.turma}'

    def fazer_matricula(self):
        print(f'A matricula de {self.nome} foi realizada')


class Professor(Pessoa):
    def __init__(self,nome, idade, especialidade, grau):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.grau = grau

    def __str__(self):
        return f'nome: {self.nome}, idade: {self.idade}, especialidade: {self.especialidade}, grau: {self.grau} '


    def darAula(self):
        print(f'a aula de {self.especialidade}, foi dada pelo professor {self.nome}')



