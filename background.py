import sys
import pygame as pg

class background(pg.sprite.Sprite):
    def __init__(self):
        self.image= pg.image.load("ex05/images/sky_img.png")#背景画像を受け取る
        self.image = pg.transform.rotozoom(self.image, 0, 2.0)#背景画像の大きさ修正
        self.rect = self.image.get_rect()

    def update(self, movevalue:float):
        self.rect.move_ip(-movevalue, 0)#横方向に画像をキャラに合わせて動かす



        
    