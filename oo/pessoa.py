class Pessoa():
    def __init__(self, nome = None, idade = 0):
        self.nome = nome

    def cumprimentar(self):
        return f'Ola Pessoa {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Elivando'
    print(p.nome)
