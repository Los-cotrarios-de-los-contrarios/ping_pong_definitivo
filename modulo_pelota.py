import random
import pygame
from pygame.locals import QUIT


# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)



class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

