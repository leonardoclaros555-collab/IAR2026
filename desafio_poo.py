class Suscripcion:

    def __init__(self, usuario, precio_base, codigo_tarjeta):
        self.usuario = usuario
        self.precio_base = precio_base
        self.__codigo_tarjeta = codigo_tarjeta

    def obtener_tarjeta(self):
        return f"XXXX-{self.__codigo_tarjeta[-4:]}"   
    
    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido estándar.")

class SuscripcionPremium(Suscripcion):

    def __init__(self, usuario, precio_base, codigo_tarjeta, calidad_video):
        super().__init__(usuario, precio_base, codigo_tarjeta)
        self.calidad_video = calidad_video   

    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido en máxima definición {self.calidad_video}.")

suscripcion1 = Suscripcion("Alexis", 9.99, "1234567812345678")

print("Tarjeta:", suscripcion1.obtener_tarjeta())
suscripcion1.reproducir_contenido()

print()

suscripcion2 = SuscripcionPremium("María", 19.99, "9876543212344321", "4K")

print("Tarjeta:", suscripcion2.obtener_tarjeta())
suscripcion2.reproducir_contenido()
    