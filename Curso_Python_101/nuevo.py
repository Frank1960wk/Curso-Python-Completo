
saludo ='Hola '
name = 'frank '
last = 'Rosas'

def mi_funcion():
    saludo = 'Que tal '
    name = 'Maitane '
    last = 'Rodriguez '
    print('n1 '+saludo + name + last)
    
    def mi_segunda_funcion():
        global last
        saludo = 'Como estas '
        name = 'Angie '
        last = 'del Bosque '
class        print ('n2 '+saludo+name)
    mi_segunda_funcion()
print(saludo+name+ last)
mi_funcion()
print(saludo+name+ last)
mi_funcion()



