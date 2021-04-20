class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá { id (self) }'

if __name__ == '__main__':
    vitor = Pessoa(nome='Vitor')
    veloso = Pessoa(vitor, nome='veloso')
    print(Pessoa.cumprimentar(veloso))
    print(id(veloso))
    print(veloso.cumprimentar())
    print(veloso.nome)
    print(veloso.idade)
    for filho in veloso.filhos:
        print(filho.nome)
        veloso.sobrenome = 'quintana'
        del veloso.filhos
        print(veloso.__dict__)
        print(vitor.__dict__)

