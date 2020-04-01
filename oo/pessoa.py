#criar uma classe.
class Pessoa:   #o nome sempre com a 1 letra maiuscula, ex: ExemploPessoa.
    def cumprimentar(self): #metodo é uma funcão da classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # todos os 3 metodos do print imprimo o mesmo metodo

