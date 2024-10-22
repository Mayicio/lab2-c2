class Papeleria:
    def __init__(self, cuadernos=0, lapices=0, precio_compra=0):
        # Inicializa los atributos de la clase Papeleria
        # cuadernos: tipo de cuaderno (50 hojas o 100 hojas)
        # lapices: tipo de lápiz (grafito o color)
        # precio_compra: precio al que se compra el artículo
        self.cuadernos = cuadernos  # Tipo de cuaderno
        self.lapices = lapices  # Tipo de lápiz
        self.marca_cuadernos = "Hojitas"  # Marca predeterminada de los cuadernos
        self.marca_lapices = "Rayas"  # Marca predeterminada de los lápices
        self.precio_compra = precio_compra  # Precio de compra del artículo
        self.precio_venta = self.calcular_precio_venta()  # Calcula el precio de venta basado en el precio de compra

    def calcular_precio_venta(self):
        # Calcula el precio de venta aplicando un margen del 30% sobre el precio de compra
        return self.precio_compra * 1.30

    def recibir_datos(self):
        # Solicita al usuario que ingrese los detalles del cuaderno y lápiz
        tipo_cuaderno = int(input("Seleccione el tipo de cuaderno (1: 50 Hojas, 2: 100 Hojas): "))
        if tipo_cuaderno == 1:
            self.cuadernos = "50 Hojas"  # Asigna el tipo "50 Hojas" si el usuario selecciona la opción 1
        elif tipo_cuaderno == 2:
            self.cuadernos = "100 Hojas"  # Asigna el tipo "100 Hojas" si el usuario selecciona la opción 2
        else:
            print("Opción no válida.")  # Muestra un mensaje si la opción no es válida

        tipo_lapiz = input("Seleccione el tipo de lápiz (grafito o color): ").lower()
        if tipo_lapiz == "grafito":
            self.lapices = "Lápiz de Grafito"  # Asigna el tipo de lápiz como "grafito"
        elif tipo_lapiz == "color":
            self.lapices = "Lápiz de Color"  # Asigna el tipo de lápiz como "color"
        else:
            print("Opción no válida.")  # Muestra un mensaje si la opción no es válida

        # Solicita el precio de compra y actualiza el precio de venta
        self.precio_compra = float(input("Ingrese el precio de compra: "))
        self.precio_venta = self.calcular_precio_venta()  # Calcula el nuevo precio de venta

    def mostrar_datos(self):
        # Muestra los detalles del artículo registrado
        print("\nDetalles del artículo registrado:")
        print(f"Marca de Cuadernos: {self.marca_cuadernos}")
        print(f"Tipo de Cuaderno: {self.cuadernos}")
        print(f"Marca de Lápices: {self.marca_lapices}")
        print(f"Tipo de Lápiz: {self.lapices}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")


# Creación de la primera instancia del artículo y se registran sus datos
articulo1 = Papeleria()
articulo1.recibir_datos()
articulo1.mostrar_datos()

# Creación de la segunda instancia del artículo y se registran sus datos
articulo2 = Papeleria()
articulo2.recibir_datos()
articulo2.mostrar_datos()

