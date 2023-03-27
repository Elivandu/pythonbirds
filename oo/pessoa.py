class Pessoa():
    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Pessoa {id(self)}'

if __name__ == '__main__':
    vando = Pessoa(nome='Vando')
    elias = Pessoa(vando, nome='Elias')
    print(Pessoa.cumprimentar(elias))
    print(id(elias))
    print(elias.cumprimentar())
    print(elias.nome)
    print(elias.idade)
    for filho in elias.filhos:
        print(filho.nome)

