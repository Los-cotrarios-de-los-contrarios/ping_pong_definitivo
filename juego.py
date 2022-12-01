# pong_1_5.py: Clase RaquetaPong
from modulo_pelota import*
import random
import pygame
from pygame.locals import QUIT


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 5")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
