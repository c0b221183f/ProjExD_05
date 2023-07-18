import sys
import random#
import pygame as pg
import character as ch
from background import background


from Gakutyou import Gakutyou # 学長クラスのインポート

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

class Enemy(pg.sprite.Sprite):
    """
    道中の障害物(おさかなさん)に関するクラス
    """

    def __init__(self):
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load("ex05/images/ojama.png"), 0, 0.5)   # 障害物の画像読み込み
        self.rect = self.image.get_rect()
        self.rect.center = WITDH / 4 * 3, HEIGHT / 4
        self.vy = +50
        self.ay = +3
        self.vx = 0#


    def update(self):
        """
        お魚が地面ではねるところ
        地面の座標(マージ前は750と仮定)に到達するまで等加速し、地面で速度を反転
        引数screen：画面Surface
        """
        if self.rect.centery >= 750:
            self.vy = -60
            self.vx = random.randint(-5, 5) * 5#
        self.vy += self.ay
        #self.rect.centerx = Character.calc_mv()   スクロールに合わせたx座標の移動(マージ後に調整)
        if (self.rect.left < 0) or (self.rect.right > WITDH):#
            self.vx *= -1#
        self.rect.centerx += self.vx#
        self.rect.centery += self.vy
        

def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)

    gakutyou = Gakutyou((1000, 200), 1) # 学長インスタンスを作成
    character = ch.Character([200, 700])
    bg = background()
    start_menu = Start_menu()

    game_state = "menu_start"
    start_menu.button(screen, 0)

    emys = pg.sprite.Group()
    emys.add(Enemy())

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            if (event.type == pg.KEYDOWN and event.key == pg.K_RIGHT):#右キーを押下で設定画面に移れる状態にする
                start_menu.button(screen, 1)
                game_state = "menu_settei"
            if(event.type == pg.KEYDOWN and event.key == pg.K_LEFT):#左キーを押下でゲーム画面に移れる状態にする
                start_menu.button(screen, 0)
                game_state = "menu_start"

            
        bg.update(1)
        screen.blit(bg.image,bg.rect)

        gakutyou.update() # 学長インスタンスの更新
        if gakutyou.get_isReady(): # 学長の攻撃中
            shadeSurface = pg.Surface((WITDH, HEIGHT))
            shadeSurface.fill((0, 0, 0))
            shadeSurface.set_alpha(100)
            screen.blit(shadeSurface, (0, 0))
        screen.blit(gakutyou.image, gakutyou.rect) # 学長インスタンスを描画
        screen.blit(character.image, character.rect)
        key_lst = pg.key.get_pressed()
  
        # キャラクターと障害物の衝突判定
        for emy in emys:
            if  character.rect.collidedict(emy.rect):
                character
            else:
                character = 10
            character.update(screen)
        
        character.calc_mv(key_lst)
        emys.update()
        emys.draw(screen)
                    
        keys = pg.key.get_pressed()
        if (keys[pg.K_SPACE] and game_state == "menu_start"): #スペースキーを押下でゲーム開始
            game_state = "game"

        if (keys[pg.K_SPACE] and game_state == "menu_settei"):#スペースキーを押下で設定画面に遷移できる状態であることをターミナルに表示
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