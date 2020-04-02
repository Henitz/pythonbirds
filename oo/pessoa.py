class Pessoa:
     def __init__(self, nome = None, idade = 35):
          self.idade = idade
          self.nome = nome
     def Cumprimentar(self):
          return f'Ola {id(self)}'

if __name__ == '__main__':
     p = Pessoa('Luciano')
     print(Pessoa.Cumprimentar(p))
     print (id(p))
     print(p.Cumprimentar())
     print (p.nome)
     p.nome = 'Renzo'
     print (p.nome)
     print(p.idade)