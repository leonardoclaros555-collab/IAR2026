class Suscripcion:

    def __init__(self, usuario, precio_base, codigo_tarjeta):
        self.usuario = usuario
        self.precio_base = precio_base
        self.__codigo_tarjeta = codigo_tarjeta

    def obtener_tarjeta(self):
        return f"XXXX-{self.__codigo_tarjeta[-4:]}"   
    
    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido estándar.")

    