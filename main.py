import sys

import pygame as pg

WITDH = 1600
HEIGHT = 900

def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_image, [0, 0])
    
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
