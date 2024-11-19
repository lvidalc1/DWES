class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 25
        self.defensa = 15
        self.salud = 100
        self.salud_maxima = 100

    def atacar(self, enemigo):
        daño = self.ataque - enemigo.defensa
        if daño > 0:
            enemigo.salud -= daño
            print(f"Héroe ataca a {enemigo.nombre}.")
            print(f"El enemigo {enemigo.nombre} ha recibido {daño} puntos de daño.")
        else:
            print(f"El enemigo ha bloqueado el ataque.")
    
    def curarse(self):
        self.salud = min(self.salud + 25, self.salud_maxima)
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    def defenderse(self):
        self.defensa += 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa}.")
    
    def reset_defensa(self):
        self.defensa = 10
        print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0
