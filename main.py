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
top = False
down = False
left = False
right = True
score1 = 0 
score2 = 0


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
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 126:
            self.rect.y += self.speed
        return self.rect.y
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 126:
            self.rect.y += self.speed
        return self.rect.y

class Ball(GameSprite):
    def update(self):
        global right
        global left
        global top
        global down
        global score1
        global score2

        if sprite.collide_rect(ten_ball, Player1) and Player1.update_l() <= self.rect.y + 25 and self.rect.y + 25 < Player1.update_l() + 45:
            top = False
            left = False
            down = True
            right = True

        if sprite.collide_rect(ten_ball, Player1) and Player1.update_l() + 45 <= self.rect.y + 25 and self.rect.y + 25 < Player1.update_l() + 91:
            top = False
            left = False
            down = False
            right = True

        if sprite.collide_rect(ten_ball, Player1) and Player1.update_l() + 91 <= self.rect.y + 25 and self.rect.y + 25 <= Player1.update_l() + 136:
            top = True
            left = False
            down = False
            right = True

        if sprite.collide_rect(ten_ball, Player2) and Player2.update_r() <= self.rect.y + 25 and self.rect.y + 25 < Player2.update_r() + 45:
            top = False
            left = True
            down = True
            right = False

        if sprite.collide_rect(ten_ball, Player2) and Player2.update_r() + 45 <= self.rect.y + 25 and self.rect.y + 25 < Player2.update_r() + 91:
            top = False
            left = True
            down = False
            right = False

        if sprite.collide_rect(ten_ball, Player2) and Player2.update_r() + 91 <= self.rect.y + 25 and self.rect.y + 25 <= Player2.update_r() + 136:
            top = True
            left = True
            down = False
            right = False

        elif self.rect.y < 0:
            top = True
            down = False
        elif self.rect.y > 450:
            top = False
            down = True

        if right == True and top == False and down == False and left == False:
            self.rect.x += self.speed
        if right == False and top == False and down == False and left == True:
            self.rect.x -= self.speed
        if right == True and top == True and down == False and left == False:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if right == True and top == False and down == True and left == False:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        if right == False and top == True and down == False and left == True:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        if right == False and top == False and down == True and left == True:
            self.rect.x -= self.speed
            self.rect.y -= self.speed

        if self.rect.x < 0:
            finish = True
            win1 = font2.render("Правый игрок выиграл!", 1, (255, 255, 255))
            window.blit(win1, (225, 225))
        if self.rect.x > 700:
            finish = True
            win2 = font2.render("Левый игрок выиграл!", 1, (255, 255, 255))
            window.blit(win2, (225, 225))

win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(bg_color)

Player1 = Player(img_player, 5, 250, 39, 136, 13)
Player2 = Player(img_player, 656, 250, 39, 136, 13)
ten_ball = Ball(img_ball, win_width / 2 - 35, win_height / 2 - 25, 50, 50, 10)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(bg_color)

        ten_ball.update()
        Player1.update_l()
        Player2.update_r()
        
        Player1.reset()
        Player2.reset()

        ten_ball.reset()
        
        display.update()
    #цикл срабатывает каждую 0.05 секунд
    time.delay(50)