#Crear un programa que elija generos de musica y sus nombres

class Musica:
    def __init__(self, genero, nombreMusica):
        self.nombreMusica = nombreMusica
        self.genero = genero
cancion1 = Musica("POP","One Kiss - Dua Lipa")
cancion2 = Musica("Electronica", "Wake Me Up - Avicci")

class musicPOP(Musica):
    pass
    def musica():
        return "\nEn el genero musical {}, esta la cancion llamada {}".format(cancion1.genero,cancion1.nombreMusica)

class musicElectronica(Musica):
    pass
    def musica():
        return "\nEn el genero musical {}, esta la cancion llamada {}".format(cancion2.genero,cancion2.nombreMusica)
    
Genero1 = musicPOP
Genero2 = musicElectronica
print(Genero1.musica())
print(Genero2.musica())