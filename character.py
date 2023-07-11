import pygame as pg
import main




class Character(pg.sprite.Sprite):
    """
    操作キャラクターに関するクラス
    """
    def __init__(self, xy: tuple[int, int]):
        """
        操作キャラクターSurfaceを描画する
        引数 xy：キャラクターの初期位置
        """
        super().__init__()
        self.image = pg.transform.flip(pg.transform.rotozoom(pg.image.load("ex05/images/character.png"), 0, 0.5), True, False)
        self.rect = self.image.get_rect()
        self.rect.center = xy
        self.dx = 10

    def calc_mv(self, key_lst: list[bool]):
        """
        押下キーに応じてキャラクターの移動量を返す関数
        引数１ key_lst：押下キーの真理値リスト
        """
        mv = 0
        # 左シフトを押すと加速
        if key_lst[pg.K_LSHIFT]:
            self.dx = 20
        else:
            self.dx = 10
        if key_lst[pg.K_LEFT]:
            mv = self.dx
        elif key_lst[pg.K_RIGHT]:
            mv = -self.dx
        return mv

    def update(self, screen: pg.Surface):
        """
        障害物に当たった時に画像を切り替える
        引数 screen：画面Surface
        """
        self.image = pg.transform.flip(pg.image.load("ex05/images/character2.png"), True, False)
        screen.blit(self.image, self.rect)

 