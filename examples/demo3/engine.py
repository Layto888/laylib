import pygame as pg
from laylib import DefaultEngine


class Game(DefaultEngine):
    # main engine
    FPS = 25

    def __init__(self):
        super().__init__()

    def new_demo(self):
        pg.mixer.music.play()
        self.all_sprites.add(MyImage(self.img[0]))
        self.playing = True

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.text = 'Sound track(seconds):  {:.2f} '.format(
            pg.mixer.music.get_pos() / 1000.0)
        self.res.fnt.render(self.fnt[0], self.text, (50, 50))
        pg.display.flip()

    def update(self):
        if not self.playing:
            self.new_demo()
        self.clock.tick(self.FPS)


class MyImage(pg.sprite.Sprite):
    def __init__(self, my_image):
        super().__init__()
        self.image = my_image
        self.rect = self.image.get_rect()
