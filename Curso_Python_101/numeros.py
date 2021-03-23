
# Global
name = 'VARIABLE GLOBAL'
def saludo():
    # Enclosing
    name = 'Eric Alexander'
    print (name)
    def hola():
        # Local
        name = 'Variable Local'
        print('Hola ' + name)

    hola ()
saludo ()
