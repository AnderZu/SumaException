class Operaciones():
    def ingresoDatos(self, dato):
        if not type(dato) is float:
            try:
                dato = float(dato)
            except ValueError:
                print(f"El parámetro \"{dato}\" no se puede convertir a float")
                exit(2)
        return dato

    def suma(self, sumando1, sumando2):
        for n in (sumando1, sumando2):
            if not isinstance(n, int) and not isinstance(n, float):
                raise ValueError
        return sumando1 + sumando2
    def resta(self, resta1, resta2):
        for n in (resta1, resta2):
            if not isinstance(n, int) and not isinstance(n, float):
                raise ValueError
        return resta1 - resta2
