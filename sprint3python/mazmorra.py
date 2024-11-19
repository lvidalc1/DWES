import random
from monstruo import Monstruo
from tesoro import Tesoro

class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Orco", 20, 5, 35),
            Monstruo("Dragón", 45, 20, 95),
            Monstruo("Golem", 35, 15, 70)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        print(f"Héroe entra en la mazmorra.")
        
        while self.heroe.esta_vivo() and self.monstruos:
            monstruo = self.monstruos.pop(0)
            print(f"Te has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)

        if self.heroe.esta_vivo():
            print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print(f"Héroe ha sido derrotado en la mazmorra.")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            
            opcion = input("Elige una opción: ")
            
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
            else:
                print(f"{enemigo.nombre} ha sido derrotado.")
                self.buscar_tesoro()
                break

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
