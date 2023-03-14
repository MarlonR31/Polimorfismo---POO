#Crear un programa que dirija la categoria de cada pelicula
class Cine:
    def __init__(self, nombre1, nombre2, nombre3, nombre4, categoria1, categoria2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.nombre3 = nombre3
        self.nombre4 = nombre4
        self.categoria1 = categoria1
        self.categoria2 = categoria2
        pass
peli = Cine("Transformers","Godzilla vs Kong","El Exorcista","La noche de los muertos vivientes", "Accion", "Terror")

class categorias(Cine):
    pass
    def cine():
        return "Categorias de peliculas \n1- {} \n2- {}".format(peli.categoria1, peli.categoria2)

class diasDisponibles(Cine):
    pass
    def cine():
        print("Dias de disponibilidad de las peliculas seran por categoria:")
        return"- Lunes, Miercoles y Viernes, Peliculas de {} \n- Martes, Jueves y Sabado, Peliculas de {}".format(peli.categoria1, peli.categoria2)

class nombresPeliculas(Cine):
    pass
    def cine():
        print("\nNombres de las peliculas, segun su categoria:")
        return "Accion: \n1- {} \n2- {} \nTerror: \n1- {} \n2- {}".format(peli.nombre1, peli.nombre2, peli.nombre3, peli.nombre4)

ver1 = categorias
ver2 = diasDisponibles
ver3 = nombresPeliculas

print(ver1.cine())
print(ver2.cine())
print(ver3.cine())
