import sys

import pygame as pg

WITDH = 1600
HEIGHT = 900

class Start_menu:
    """
    スタート画面を表示させるクラス
    """
    def __init__(self):
        """
        フォント、メニュータイトルの表示
        """
        self.font = pg.font.Font("ex05/fonts/onryou.TTF", 100)
        self.menu_title = self.font.render("学長から見つかるな！", True, (255, 255, 255))
        
    def button(self, screen: pg.Surface, num:int):
        """
        どのボタンを選択しようとしているのかを表示する
        引数1 screen 画面の表示
        引数2 num どのボタンが選択中か
        """
        if num == 0:
            self.start_button = self.font.render("スタート", True, (255, 0, 0))
            self.hoge_button = self.font.render("セッテイ",True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(self.menu_title, (WITDH/2 - self.menu_title.get_width()/2, HEIGHT/2 - self.menu_title.get_height()))
            screen.blit(self.start_button, (WITDH/3 - self.start_button.get_width()/2, HEIGHT/2 + self.start_button.get_height()))
            screen.blit(self.hoge_button, (WITDH/2 + self.hoge_button.get_width()/2, HEIGHT/2 + self.start_button.get_height()))
        
        if num == 1:
            self.start_button = self.font.render("スタート", True, (255, 255, 255))
            self.hoge_button = self.font.render("セッテイ",True, (255, 0, 0))
            screen.fill((0, 0, 0))
            screen.blit(self.menu_title, (WITDH/2 - self.menu_title.get_width()/2, HEIGHT/2 - self.menu_title.get_height()))
            screen.blit(self.start_button, (WITDH/3 - self.start_button.get_width()/2, HEIGHT/2 + self.start_button.get_height()))
            screen.blit(self.hoge_button, (WITDH/2 + self.hoge_button.get_width()/2, HEIGHT/2 + self.start_button.get_height()))

def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)

    start_menu = Start_menu()

    game_state = "menu_start"
    start_menu.button(screen, 0)

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if (event.type == pg.KEYDOWN and event.key == pg.K_RIGHT):
                start_menu.button(screen, 1)
                game_state = "menu_settei"
            if(event.type == pg.KEYDOWN and event.key == pg.K_LEFT):
                start_menu.button(screen, 0)
                game_state = "menu_start"

        keys = pg.key.get_pressed()
        if (keys[pg.K_SPACE] and game_state == "menu_start"):
            game_state = "game"

        if (keys[pg.K_SPACE] and game_state == "menu_settei"):
            print("settei")
       
        if game_state == "game":
            screen.blit(bg_image, [0, 0])

        
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
