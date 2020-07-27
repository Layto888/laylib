import pygame as pg
from laylib import DefaultEngine


class Engine(DefaultEngine):
    """
    In this demo we display an image, we print text and we
    play all the music list in loop with a time limit of 5s for each sound.
    """
    FPS = 25
    PLAY_TIME = 5000

    def __init__(self):
        super().__init__()

    def new_demo(self):
        # let's choose the image with index = 10 ('bidoubird.jpg')
        self.all_sprites.add(MyImage(self.img[0]))
        # this starts the main loop
        self.playing = True
        # to count the elapsed time when playing music
        self.elapsed = 0.0
        # choose an index in list of music and play it.
        self.music_index = 0
        # start play
        self.res.msc.play(self.msc[self.music_index], 0.5)

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.text = 'Playing: {} - Next Sound in: {:.2f} '.format(
            self.msc[self.music_index], self.elapsed / 1000.0)
        # print text with res.fnt object.
        self.res.fnt.render(self.fnt[0], self.text, (50, 50))
        pg.display.flip()

    def update(self):
        if not self.playing:
            self.new_demo()
        # play next track ?
        self.elapsed = self.PLAY_TIME - pg.mixer.music.get_pos()
        if self.elapsed <= 0.0:
            # jump to next track
            self.music_index += 1
            # play all musics and back to the first.
            self.music_index %= len(self.msc)
            self.res.msc.play(self.msc[self.music_index], 0.5)
        self.clock.tick(self.FPS)


class MyImage(pg.sprite.Sprite):
    def __init__(self, my_image):
        super().__init__()
        self.image = my_image
        self.rect = self.image.get_rect()
