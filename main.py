import sys

import pygame as pg
import character as ch

WIDTH = 1600
HEIGHT = 900


def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)
    character = ch.Character([200, 700])

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_image, [0, 0])
        screen.blit(character.image, character.rect)
        key_lst = pg.key.get_pressed()
        """
        # キャラクターと障害物の衝突判定
        for emy in emys:
            if  character.rect.collidedict(emy.rect):
                character
            else:
                character = 10
            character.update(screen)
        """

        character.calc_mv(key_lst)
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
