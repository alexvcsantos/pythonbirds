#criar uma classe.
class Pessoa:   #o nome sempre com a 1 letra maiuscula, ex: ExemploPessoa.
    def __init__(self, nome=None, idade=35):  #para criar atributos de um metodo, é usado um metodo especial, jaá pode criar um atributo e definir o valor nulo.
        self.idade = idade
        self.nome = nome   #para criar um atributo de um objeto utiliza self.atributo = None ou seja nulo
    def cumprimentar(self): #metodo é uma funcão da classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # todos os 3 metodos do print imprimo o mesmo metodo
    print(p.nome)
    p.nome = 'Alex' #alterar o conteudo do atributo
    print(p.nome)
    print(p.idade)

