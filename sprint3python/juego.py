import random

class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 20
        self.defensa = 10
        self.salud = 100
        self.salud_maxima = 100

    def atacar(self, enemigo):
        daño = self.ataque - enemigo.defensa
        if daño > 0:
            enemigo.salud -= daño
            print(f"{self.nombre} ataca a {enemigo.nombre} y le hace {daño} de daño.")
        else:
            print(f"{enemigo.nombre} bloquea el ataque.")

    def curarse(self):
        self.salud = min(self.salud + 20, self.salud_maxima)
        print(f"{self.nombre} se cura. Salud: {self.salud}")

    def defenderse(self):
        self.defensa += 5
        print(f"{self.nombre} se defiende. Defensa temporal aumentada a {self.defensa}.")

    def reset_defensa(self):
        self.defensa -= 5
        print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0


class Monstruo:
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atacar(self, heroe):
        daño = self.ataque - heroe.defensa
        if daño > 0:
            heroe.salud -= daño
            print(f"{self.nombre} ataca a {heroe.nombre} y le hace {daño} de daño.")
        else:
            print(f"{heroe.nombre} bloquea el ataque.")

    def esta_vivo(self):
        return self.salud > 0


class Tesoro:
    def __init__(self):
        self.beneficios = ['aumento de ataque', 'aumento de defensa', 'restauración de salud']

    def encontrar(self, heroe):
        beneficio = random.choice(self.beneficios)
        if beneficio == 'aumento de ataque':
            aumento = random.randint(5, 10)#randit: método que devuelve un número entero del elemento seleccionado del rango especificado.
            heroe.ataque += aumento
            print(f"{heroe.nombre} encuentra un tesoro: Aumento de ataque a {heroe.ataque}.")
        elif beneficio == 'aumento de defensa':
            aumento = random.randint(5, 10)
            heroe.defensa += aumento
            print(f"{heroe.nombre} encuentra un tesoro: Aumento de defensa a {heroe.defensa}.")
        else:
            heroe.salud = heroe.salud_maxima
            print(f"{heroe.nombre} encuentra un tesoro: Salud restaurada a {heroe.salud}.")


class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Golem de Piedra", 30, 40, 80),
            Monstruo("Orco", 25, 15, 60),
            Monstruo("Basilisco", 35, 20, 70)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        print(f"{self.heroe.nombre} entra en la mazmorra.")
        while self.monstruos and self.heroe.esta_vivo():
            monstruo = self.monstruos.pop(0)
            print(f"\nTe has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)
            if self.heroe.esta_vivo():
                self.tesoro.encontrar(self.heroe)

        if self.heroe.esta_vivo():
            print(f"\n¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print(f"\n{self.heroe.nombre} ha sido derrotado.")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.heroe.atacar(enemigo)
            elif opcion == "2":
                self.heroe.defenderse()
            elif opcion == "3":
                self.heroe.curarse()
            else:
                print("Opción no válida.")
                continue

            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)
            
            self.heroe.reset_defensa()  # Reset defensa después de cada turno


if __name__ == "__main__":
    nombre_heroe = input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre_heroe)
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()
