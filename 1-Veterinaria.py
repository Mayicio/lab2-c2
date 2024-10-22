class Veterinaria:
    def __init__(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        # Inicialización de atributos de la clase
        # peso: peso de la mascota en kg
        # nombre: nombre de la mascota
        # clase: raza de la mascota
        # color: color del pelaje de la mascota
        # edad: edad de la mascota en años
        # genero: género de la mascota (macho/hembra)

        self.Estado = "NO ATENDIDO"  # Estado inicial de la mascota al no estar atendida
        self.peso = peso  # Peso de la mascota
        self.tamano = self.determinar_tamano()  # Se determina el tamaño de la mascota en función de su peso
        self.Nombre = nombre  # Nombre de la mascota
        self.Clase = clase  # Raza de la mascota
        self.Color = color  # Color de la mascota
        self.Edad = edad  # Edad de la mascota
        self.Genero = genero  # Género de la mascota

    def determinar_tamano(self):
        # Determina el tamaño de la mascota según su peso
        if self.peso <= 10:
            return "Perro Pequeño"  # Si pesa 10 kg o menos, es un perro pequeño
        else:
            return "Perro Grande"  # Si pesa más de 10 kg, es un perro grande

    def cambiar_estado(self):
        # Cambia el estado de la mascota a 'ATENDIDO'
        self.Estado = "ATENDIDO"
        return self.Estado  # Retorna el nuevo estado de la mascota

    def entrada_datos(self):
        # Solicita la entrada de datos del usuario para asignar los atributos de la mascota
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.Genero = input("Ingrese el género de su mascota: ")
        self.tamano = self.determinar_tamano()  # Vuelve a determinar el tamaño según el peso ingresado

    def muestra_datos(self):
        # Muestra los datos de la mascota
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.Genero}")
        print(f"Estado: {self.Estado}")


perro = Veterinaria()  # Se puede crear la instancia sin valores iniciales
perro.entrada_datos()  # Se piden los datos al usuario
perro.cambiar_estado()  # Cambia el estado a "ATENDIDO"
perro.muestra_datos()  # Muestra todos los datos del perro
