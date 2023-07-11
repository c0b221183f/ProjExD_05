import sys
import pygame as pg

class background(pg.sprite.Sprite):
    def __init__(self):
        self.image= pg.image.load("ex05/images/sky_img.png")
        self.rect = self.image.get_rect()

    def update(self,movevalue:float):
        self.rect.move_ip(-movevalue,0)



        
    