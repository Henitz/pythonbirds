class Pessoa:
     def Cumprimentar(self):
          return f'Ola {id(self)}'

if __name__ == '__main__':
     p = Pessoa()
     print(Pessoa.Cumprimentar(p))
     print (id(p))
     print(p.Cumprimentar())