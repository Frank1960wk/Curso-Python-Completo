numero = [1, 2, 3, 4, 5, 6, 7]

# Global
name = 'VARIABLE GLOBAL'


def saludo():
    # Enclosing
    name = 'Eric Alexander'

    def hola():
        # Local
        name = 'Variable Local'
        print('Hola ' + name)

    hola


saludo
