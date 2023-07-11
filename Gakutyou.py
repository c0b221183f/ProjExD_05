import pygame as pg

class Gakutyou(pg.sprite.Sprite):

    BACK_COLOR = (120, 250, 120)
    COOL_TIME = 480

    def __init__(self, position: tuple[int, int], size: float) -> None:
        super().__init__()
        gImg = pg.image.load("images/gakutyou.png")
        cImg = pg.image.load("images/g_cloud.png")
        self.image = pg.Surface((300, 340))
        self.image.fill(Gakutyou.BACK_COLOR)
        self.image.blit(pg.transform.rotozoom(gImg, 0, 300 / gImg.get_width() * 1.9), (-210,-70))
        self.image.blit(pg.transform.rotozoom(cImg, 0, 340 / cImg.get_width() * 1.05), (-25,65))
        self.rect = self.image.get_rect()
        self.rect.center = position

        eyeLight = pg.image.load("images/eye_light.png")
        eyeLight = pg.transform.rotozoom(eyeLight, 0, 0.035)
        self.images: list[pg.surface.Surface] = []
        for i in range(50):
            currentImg = self.image.copy()
            currentSurf = pg.Surface((300, 100))
            currentSurf.blit(eyeLight, (117, 40))
            currentSurf.blit(eyeLight, (150, 40))
            currentSurf.set_colorkey((0, 0, 0))
            currentSurf.set_alpha(i * 5)
            currentImg.blit(currentSurf, (0, 0))
            self.images.append(currentImg)
        for i in range(20):
            self.images.append(self.images[49].copy())
        for i in range(50)[::-1]:
            self.images.append(self.images[i].copy())
        self.images = [pg.transform.rotozoom(x, 0, size) for x in self.images]
        for i in self.images:
            i.set_colorkey(Gakutyou.BACK_COLOR)
        self.image = self.images[0]
        self.timer = 0
        self.attackTimer = -1
        self.isReady = False

    def update(self):
        """
        update関数のオーバーライド\n
        毎フレーム呼び出してください
        """
        if self.timer >= Gakutyou.COOL_TIME or self.isReady:
            self.timer = 0
            self.isReady = True
            self.image = self.images[50]
        else:
            self.timer += 1
            self.image = self.images[int(self.timer * ((self.timer // 120 + 1) ** 2)) % 120]
            if int(self.timer * ((self.timer // 120 + 1) ** 2)) % 120 <= 10:
                pg.mixer.init()
                pg.mixer.music.load("sounds/pika.mp3")
                pg.mixer.music.play(1)
        
    def get_isReady(self):
        """
        クールタイムが終わったかをBool型で返す関数、Trueの時呼び出されると一定時間Trueを返し続ける\n
        引数：無し\n
        戻り値：True(攻撃できるとき) or False(攻撃できないとき)
        """
        if self.attackTimer >= 0:
            self.attackTimer -= 1
            if self.attackTimer < 0:
                self.isReady = False
            return True
        elif self.isReady:
            self.attackTimer = 100
            return True
        else:
            return False
    
    def finished_attack(self):
        self.isReady = False
