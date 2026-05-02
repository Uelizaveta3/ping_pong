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
font2 = font.Font(None,30)

i1 = 0
i2 = 0

lose_1 = font1.render(
    'игрок 1 проиграл', True, (255, 49, 0)
)

lose_2 = font1.render(
    'игрок 2 проиграл', True, (255, 49, 0)
)

# count1 = font2.render(
#     'счет игрока 1:'+str(i1), True, (255,255,255)
# )
# count2 = font2.render(
#     'счет игрока 2:'+str(i2), True, (255,255,255)
# )
count = font2.render(
    'счет:'+str(i1)+':'+str(i2), True, (255,255,255)
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
        main_win.fill((0, 183, 74))
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        raketka_1.update_l()
        raketka_1.reset()
        raketka_2.update_r()
        raketka_2.reset()
#         count1 = font2.render(
#     'счет игрока 1:'+str(i1), True, (255,255,255)
# )
#         count2 = font2.render(
#     'счет игрока 2:'+str(i2), True, (255,255,255)
# )
        count = font2.render(
    'счет:'+str(i1)+':'+str(i2), True, (255,255,255)
)

        if ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball,raketka_1) or sprite.collide_rect(ball,raketka_2):
            speed_x *= -1 

        if ball.rect.x < 0:
            # main_win.blit(lose_1,(120,225))
            i2 += 1
            ball.rect.x = 300
            ball.rect.y = 250

        if ball.rect.x > 750:
            # main_win.blit(lose_2,(120,225))
            i1 += 1
            ball.rect.x = 300
            ball.rect.y = 250
        if i1 >= 5:
            main_win.blit(lose_2,(120,225))
            speed_y = 0
            speed_x = 0
        if i2 >= 5:
            main_win.blit(lose_1,(120,225))
            speed_y = 0
            speed_x = 0
        main_win.blit(count,(5,5))
        # main_win.blit(count2,(5,30))
    display.update()
    
    
