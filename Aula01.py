class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade

    @classmethod
    def metodo(cls):
        print('Olá ')

    @classmethod
    def idade_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)

p1= Pessoa('Yago', 19)
p2= Pessoa.idade_50('viviane')
p3= Pessoa('Anonima', 34)
p4= Pessoa.criar_sem_nome(33)

print(p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
