#criar uma classe.
class Pessoa:   #o nome sempre com a 1 letra maiuscula, ex: ExemploPessoa.
    # para criar atributos de um metodo, é usado um metodo especial, jaá pode criar um atributo e definir o valor nulo.
    def __init__(self, *filhos, nome=None, idade=35):  #*filhos atributo variavel
        self.idade = idade
        self.nome = nome   #para criar um atributo de um objeto utiliza self.atributo = None ou seja nulo
        self.filhos = list(filhos)
    def cumprimentar(self): #metodo é uma funcão da classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    alex = Pessoa(nome='Alex')
    luciano = Pessoa(alex, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) # todos os 3 metodos do print imprimo o mesmo metodo
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

