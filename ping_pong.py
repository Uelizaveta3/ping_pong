from pygame import *

main_win = display.set_mode((700,500))
display.set_caption('Пинг Понг')

# background = transform.scale(
#     image.load('galaxy.jpg')
# , (700,500))

class GameSprite(sprite.Sprite):
    def __init__ (self, speed, x, y, img, size=(65,70)):
        super().__init__()
        self.speed = speed
        self.size = size
        self.image = transform.scale(
            image.load(img), self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed


game = True

while game:
    pass