class Calculadora:
    # iniciamps con el método __init__
    def __init__(self):
        self.numero1=float(input("Ingrese el primer numero: "))
        self.numero2=float(input("Ingrese el segundo numero: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        print("Numero 1: ",self.numero1)
        print("Numero 2: ",self.numero2)
        
# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona

class Ecuaciones(Calculadora):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()

    # Funcion de sumar
    def suma(self):
        self.suma=self.numero1+self.numero2
        print("El resultado de la suma de los numeros fue: ",self.suma)

    # Funcion de restar
    def resta(self):
        self.resta=self.numero1-self.numero2
        print("El resultado de la resta de los numeros fue: ",self.resta)

    #Funcion de multiplicar
    def multiplicacion(self):
        self.multiplicacion=self.numero1*self.numero2
        print("El resultado de la multiplicacion de los numeros fue: ",self.multiplicacion)

    #Funcion de division
    def division(self):
        self.division=self.numero1/self.numero2
        print("El resultado de la division de los numeros fue: ",self.division)

    #Funcion para mostrar
    def mostrar(self):
        print("Los numeros son: ")
        super().mostrar()

#Bloque principal
ecuaciones1=Ecuaciones()
ecuaciones1.mostrar()
ecuaciones1.suma()
ecuaciones1.resta()
ecuaciones1.multiplicacion()
ecuaciones1.division()
