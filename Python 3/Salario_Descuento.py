class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)

# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
        self.descuento= self.sueldo*0.035
        self.sueldo_final= self.sueldo-self.descuento

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Decuento: ",self.descuento)

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def total(self):
        if self.sueldo >= 3600000:
            print("Sr@ su descuento es de $ ",self.descuento," y Su salario total seria de $ ",self.sueldo_final)
        else:
            print("Sr@ "+self.nombre+" Usted no cuenta con descuento alguno.")
# bloque principal
empleado1=Empleado()
empleado1.mostrar()
empleado1.total()
