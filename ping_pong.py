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

ball = Player(1,300,250,'ball.png',(65,50))
raketka_1 = Player(1,-10,200,'raketka.png',(150,145))
raketka_2 = Player(1,580,200,'raketka.png',(150,145))

#шрифты
font.init()
font1 = font.Font(None,80)
lose_1 = font1.render(
    'игрок 1 проиграл', True, (139, 0, 0)
)

lose_2 = font1.render(
    'игрок 2 проиграл', True, (139, 0, 0)
)

#звуки
mixer.init()


game = True
finish = False

speed_x = 1
speed_y = 1


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        main_win.fill((0, 255, 255))
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        raketka_1.update_l()
        raketka_1.reset()
        raketka_2.update_r()
        raketka_2.reset()

        if ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball,raketka_1) or sprite.collide_rect(ball,raketka_2):
            speed_x *= -1 

        if ball.rect.x < 0:
            main_win.blit(lose_1,(120,225))
        if ball.rect.x > 750:
            main_win.blit(lose_2,(120,225))
    display.update()
    
    
