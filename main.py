from pygame import *
from random import randint
import time as tim

#фоновая музыка
mixer.init()

#шрифты и надписи
font.init()
font2 = font.Font(None, 36)

bg_color = (0, 170, 255)
img_player = "racket.png"
img_ball = 'tenis_ball.png'
move_h = True
move_h1 = False


#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 153:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 153:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.y > 50:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.rect.y < 600:
            self.rect.x -= self.speed
            self.rect.y -= self.speed

win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(bg_color)

Player1 = Player(img_player, 5, win_height / 2, 39, 136, 13)
Player2 = Player(img_player, 700 - 39 - 5, win_height / 2, 39, 136, 13)
ten_ball = Ball(img_ball, win_width / 2 - 35, win_height / 2 - 25, 50, 50, 10)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(bg_color)

        Player1.update_l()
        Player2.update_r()
        ten_ball.update()

        Player1.reset()
        Player2.reset()
        ten_ball.reset()
        display.update()
    #цикл срабатывает каждую 0.05 секунд
    time.delay(50)