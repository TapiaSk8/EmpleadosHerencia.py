#Crear clase empleados
class empleados:
    def __init__(self, nombre, puesto, usuario):
        self.nombre = nombre
        self.puesto = puesto
        self.usuario = usuario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nPuesto: {self.puesto}\nUsuario: {self.usuario}\n-----------------")

# Crear instancias de empleados
empleado1 = empleados("Edgar Hernández", "Gerente", "EHernandez1")    
empleado2 = empleados("Yareli Sanchez", "Asesor@", "YSanchez1")
empleado3 = empleados("Silvia Tapia", "Asesor@", "STapia1")
empleado4 = empleados("Juan Perez", "RH", "JPerez1")
#Crear lista de empleados
empleados_lista = [empleado1, empleado2, empleado3, empleado4]

# Mostrar la información de los empleados con un bucle for iterado en una lista de los empleados
for empleado in empleados_lista:
    empleado.mostrar_info()

# crear subclase llamada Gerente
class gerente(empleados):
    def __init__(self, nombre, departamento, usuario):
        super().__init__(nombre, "Gerente", usuario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}\n")

# crear una instancia de la sub clase  Gerente
gerente1 = gerente("Edgar Hernández", "Jurídico", "EHernandez1")
gerente1.mostrar_info()

# crear subclase: para los asesores
class Asesor(empleados):
    def __init__(self, nombre, area, usuario):
        super().__init__(nombre, "Asesor", usuario)
        self.area = area

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Área: {self.area}\n")

# Crear instancias de la clase Asesor
asesor1 = Asesor("Silvia Tapia", "Legal", "STapia1")
asesor2 = Asesor("Yareli Sanchez", "Ventas", "YSanchez1")


# Mostrar la información de los asesores
asesor1.mostrar_info()
asesor2.mostrar_info()


# Crear subclase para empleado de Recursos Humanos
class RH(empleados):
    def __init__(self, nombre, Area, usuario):
        super().__init__(nombre, "Recursos Humanos", usuario)
        self.Area = Area

    def mostrar_info(self):

        super().mostrar_info()
        print(f"Area: {self.Area}\n")

# Crear instancias de la clase RH
rh1 = RH("Juan Perez", "Recursos Humanos", "JPerez1")


# Mostrar la información de los empleados de RH
rh1.mostrar_info()
