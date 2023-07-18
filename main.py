import sys

import pygame as pg
import character as ch

from Gakutyou import Gakutyou # 学長クラスのインポート

WITDH = 1600
HEIGHT = 900


def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("images/sky_img.png"), 0, 1.35)

    gakutyou = Gakutyou((1000, 200), 1) # 学長インスタンスを作成
    character = ch.Character([200, 700])

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_image, [0, 0]

        gakutyou.update() # 学長インスタンスの更新
        if gakutyou.get_isReady(): # 学長の攻撃中
            shadeSurface = pg.Surface((WITDH, HEIGHT))
            shadeSurface.fill((0, 0, 0))
            shadeSurface.set_alpha(100)
            screen.blit(shadeSurface, (0, 0))
        screen.blit(gakutyou.image, gakutyou.rect) # 学長インスタンスを描画
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
