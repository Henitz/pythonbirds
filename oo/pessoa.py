class Pessoa:
     olhos = 2
     def __init__(self, *filhos, nome=None, idade=35):
          self.idade = idade
          self.nome = nome
          self.filhos = list(filhos)
     def Cumprimentar(self):
          return f'Ola {id(self)}'

     @staticmethod
     def metod_estatico():
          return 42
     @classmethod
     def nome_e_atributos_de_classe(cls):
          return f' (cls) - olhos {cls.olhos}'

if __name__ == '__main__':
     renzo  = Pessoa(nome='Renzo')
     luciano = Pessoa(renzo, nome='Luciano')
     print(Pessoa.Cumprimentar(luciano))
     print (id(luciano))
     print(luciano.Cumprimentar())
     print (luciano.nome)
     print (luciano.idade)
     for filho in luciano.filhos:
          print(filho.nome)
     luciano.sobrenome = 'Ramalho'
     del luciano.filhos


     print(luciano.__dict__)
     print(renzo.__dict__)
     print(Pessoa.olhos)
     print (luciano.olhos)
     print (renzo.olhos)




     print(id(Pessoa.olhos), id(luciano.olhos),id(renzo.olhos))

     print(Pessoa.metod_estatico(), luciano.metod_estatico())
   #  print(Pessoa.nome_e_atributos_de_classe(),Luciano.metodo_estatico())

