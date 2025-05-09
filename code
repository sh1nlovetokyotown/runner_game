from pygame import *
clock = time.Clock()
FPS = 60
from random import randint

class Gamesprite(sprite.Sprite):

    def __init__(self,player_x,player_y,player_image,player_speed,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and player1.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and player1.rect.x < 930:
            self.rect.x += self.speed
        if key_pressed[K_s] and player1.rect.y < 930:
            self.rect.y += self.speed
        if key_pressed[K_w] and player1.rect.y > 0:
            self.rect.y -= self.speed 
        key_pressed = key.get_pressed()

class wall(sprite.Sprite):
    def __init__(self,pos_x,pos_y,speed,size):
        sprite.Sprite.__init__(self)
        wall = Surface(size)
        wall.fill(( 255, 7, 58))
        self.image = transform.scale(wall,size)
        self.size = size
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 1000:
            self.kill()
        else:
            self.rect.y += self.speed

class enemy(Gamesprite):
    def update(self):
        self.rect.x += (player1.rect.x - self.rect.x)/30
        self.rect.y += (player1.rect.y - self.rect.y)/30


    



window = display.set_mode((1000,1000),flags = RESIZABLE)
display.set_caption('догонялки')
background = transform.scale(image.load('i.webp'),(1000,1000))

global player1
player1 = player(500,900,'faicet_higets_lvl.webp',15,65,65)
enemys = sprite.Group()
global enemy1
enemy1 = enemy(randint(100,200),randint(100,200),'angry.jpg',5,50,50)
enemys.add(enemy1)
global portal
portal = Gamesprite(350,0,"portal.webp",0,300,200)
kd = 100
laser_num = 0
win_num = 3
remove = 1
enemys_update = False
game = True
lasers_update = False
while game:
    window.blit(background,(0,0))
    clock.tick(FPS)
    if win_num == 3:
        portal.update()
        portal.reset()
    player1.update()
    player1.reset()
    if kd >= 100 and laser_num < 3 and lasers_update == True:
        wall_num = randint(1,3)
        if wall_num == 1:
            wall1 = wall(0,-20,5,(700,20))
            wall2 = wall(850,-20,5,(150,20))
        if wall_num == 2:
            wall1 = wall(0,-20,5,(150,20))
            wall2 = wall(300,-20,5,(700,20))
        if wall_num == 3:
            wall1 = wall(0,-20,5,(425,20))
            wall2 = wall(575,-20,5,(425,20))
        kd = 0
        kd += 1
        laser_num += 1

    if lasers_update == True:
        wall1.update()
        wall1.reset()
        wall2.update()
        wall2.reset()

    if win_num < 1 and enemys_update == True:
        enemy1.update()
        enemy1.reset()

    if lasers_update == True:
        if sprite.collide_rect(player1,wall1) or sprite.collide_rect(player1,wall2):
            game = False
            
    if sprite.collide_rect(player1,enemy1):
        win_num += 1
    kd += 1
    
    if sprite.collide_rect(player1,portal) and win_num == 3:
        player1.rect.x = 500
        player1.rect.y = 900
        enemys_update = True
        lasers_update = True
        win_num = 0




    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()    

