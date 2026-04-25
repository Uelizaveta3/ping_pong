from pygame import *

main_win = display.set_mode((700,500))
display.set_caption('Ping Pong')

class GameSprite(sprite.Sprite):
    def __init__ (self, speed, x, y, img, size):
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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

#шрифты
font.init()
# lose_1 = font.render(
#     'игрок 1 проиграл', True, (139, 0, 0)
# )

# lose_2 = font.render(
#     'игрок 2 проиграл', True, (139, 0, 0)
# )

#звуки
mixer.init()


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        main_win.fill((0, 255, 255))
    display.update()
    
    
