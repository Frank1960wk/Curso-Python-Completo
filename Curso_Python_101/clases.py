
class Animal():

  def __init__(self):
    print('Animal creado ')

  def quien_soy(self):
    print('Soy un animal ')

  def comer(self):
    print('estoy comiendo ')


class Perro(Animal):
  def __init__(self, name):
    Animal.__init__(self)
    self.name=name
    print('perro credo ')

  def quien_soy(self):
    print('Soy un perro ')  

huskie = Perro('Sam')
print (huskie.name)
huskie.quien_soy()
