class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'olá { id (self) }'

if __name__ == '__main__':
    p = Pessoa('vitor')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = ' joao'
    print(p.nome)

