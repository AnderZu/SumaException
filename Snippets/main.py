from src.logica.Operaciones import Operaciones


if __name__ == '__main__':
    operacion = Operaciones()

    try:
        sumando1 = operacion.ingresoDatos(input("ingrese el primer sumando  : "))
        sumando2 = operacion.ingresoDatos(input("ingrese el segundo sumando : "))
        resultado=operacion.suma(sumando1,sumando2)
        print ( "{0:.2f} + {1:.2f} = {2:.2f}".format ( sumando1 , sumando2, resultado ) )
    except ValueError:
        print("Los operandos tiene que ser numeros: {0} + {1} ".format(sumando1, sumando2))
        # raise ValueError

    sumando1 = "a"
    sumando2 = 4
    try:
        resultado = operacion.suma(sumando1,sumando2)
        print ( "{0:.2f} + {1:.2f} = {2:.2f}".format ( sumando1 , sumando2, resultado ) )
    except ValueError:
        print("Los operandos tiene que ser numeros: {0} + {1} ".format(sumando1, sumando2))

