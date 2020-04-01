#criar uma classe.
class Pessoa:   #o nome sempre com a 1 letra maiuscula, ex: ExemploPessoa.
    olhos = 2 # para criar um atributo default/ classe, assim usando menos memoria
    # para criar atributos de um metodo, é usado um metodo especial, já pode criar um atributo e definir o valor nulo.
    def __init__(self, *filhos, nome=None, idade=35):  #*filhos atributo variavel
        self.idade = idade
        self.nome = nome   #para criar um atributo de um objeto utiliza self.atributo = None ou seja nulo
        self.filhos = list(filhos)
    def cumprimentar(self): #metodo é uma funcão da classe
        return f'olá {id(self)}'

    # metodo de classe decorator
    @staticmethod
    def metodo_estatico():
        return 42
    # metodo utilizado quando quer acessar dados da propria classe
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    luciano.sobrenome = 'Ramalho' #posso criar uma variavel a qualquer momento.porem sera só para o objeto que escolhi
    del luciano.filhos #remove o atributo que inclusive foi criado no init
    #__dict__ atributo pra conferir todos os atributos de uma instancia
    print(luciano.__dict__) # tem os atributos da classe + o dinamico criado
    print(alex.__dict__) # tem só os atributos da classe
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(alex.olhos)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
