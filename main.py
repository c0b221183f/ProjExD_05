import sys

import pygame as pg
import random

WITDH = 1600
HEIGHT = 900
STAGE_WIDTH = 10000  # ステージの横幅
TREE_BOTTOM = 100
WALL_NUM = 10  # 木の数
PLAYER_SPEED = 100
trees = list()  # 木のリスト

class Wall:
    """
    遮蔽物(以下、木)の描画、判定処理
    """
    def __init__(self, screen: pg.Surface):
        """
        遮蔽物(木)を描画
        引数: screen: 画面Surface
        """
        self.tree = pg.transform.rotozoom(pg.image.load("ex05/images/tree.png"), 0, 0.5)  # 木の画像を読み込む
        screen.blit(self.tree, [WITDH, HEIGHT - 569])  # 木を表示
        self.rect = self.tree.get_rect()  # 木のrectを作成
        self.rect.bottom = HEIGHT - TREE_BOTTOM  # 木のY座標を固定
        self.rect.centerx = random.randint(500, STAGE_WIDTH)  # 木のX座標を決定。500～ステージのサイズの間にランダムで生成
    
    def update(self, key_lst: list[bool], screen: pg.Surface):
        """
        ユーザの操作に応じで木の描画位置を変更
        引数1 key_lst: 押下キーの真理値リスト
        引数2 screen: 画面Surface
        """
        self.speedx = 0  # もし、キーボードを押していなければ移動しない
        if key_lst[pg.K_LEFT]:  # もし、左矢印を押していたら...
            self.speedx = PLAYER_SPEED  # 右に20動く
        if key_lst[pg.K_RIGHT]:  # もし、右矢印を押していたら...
            self.speedx = PLAYER_SPEED * (-1)  # 左に20動く

        self.rect.centerx += self.speedx  # 木の位置を更新
        screen.blit(self.tree, self.rect)  # 更新後の木を描画
    
    
# Characterクラスと合わせてないと動かない
#    def check_player_hide_tree(self, player: Character) -> bool:
#        """
#        プレイヤーが木に隠れているかを判定する
#        引数 player: プレイヤーのSurface
#        戻り値 プレイヤーが木に隠れいているか(True隠れている, False->隠れていない)
#        """
#
#        is_hide_tree = False  # プレイヤーが木に隠れているか(True>隠れている, False->隠れていない)
#        for tree in trees:
#            if tree.rect.colliderect(player.rct):
#                is_hide_tree = True
#
#        return is_hide_tree



def main():
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))
    bg_image = pg.transform.rotozoom(pg.image.load("ex05/images/sky_img.png"), 0, 1.35)
    tmr = 0
    clock = pg.time.Clock()
    for i in range(WALL_NUM):  # WALL_NUMの分だけ繰り返す
        trees.append(Wall(screen))  # 木の情報を追加

    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.blit(bg_image, [0, 0])

        for tree in trees:  # 木を1つ1つ取得
            tree.update(key_lst, screen)  # 木の位置を更新する
        pg.display.update()
        tmr += 1
        clock.tick(50)
        print(tmr)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
