class Alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno: ")

    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)

# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Estudiante(Alumno):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        nota1=float(input("Ingrese la Primera nota: "))
        nota2=float(input("Ingrese la Segunda nota: "))
        nota3=float(input("Ingrese la Tercera nota: "))
        self.promedio =(nota1+nota2+nota3)/3

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("El promedio es: ",self.promedio)
        
    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def definitiva(self):
        if self.promedio >= 3.0:
            print("El estudiante ",self.nombre," a aprobado con ",self.promedio," ¡FELICIDADES!")
        else:
            print("El estudiante ",self.nombre," a reprobado con",self.promedio)
            
# bloque principal
estudiante1=Estudiante()
estudiante1.definitiva()
