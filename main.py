from pygame import *
clock = time.Clock()
FPS = 60
from random import randint
mixer.init()
move = True


class Gamesprite(sprite.Sprite):

    def __init__(self,player_x,player_y,player_image,player_speed,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.cur_reload_time = 0
        self.reload_time = 0.15
        self.reloading = False
        self.move = True
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and player1.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and player1.rect.x < 950:
            self.rect.x += self.speed
        if key_pressed[K_s] and player1.rect.y < 950:
            self.rect.y += self.speed
        if key_pressed[K_w] and player1.rect.y > 0:
            self.rect.y -= self.speed 
        key_pressed = key.get_pressed()
    def fire(self):
        if mouse.get_pressed()[0] and self.reloading == False:
            bullet_t = bullet(self.rect.centerx,self.rect.top,'gray_cube.jpg',10,20,20)
            bullets.add(bullet_t)
            mixer.music.load('fire.ogg')
            mixer.music.play()
            self.reloading = True
        else:
            if self.cur_reload_time < self.reload_time:
                self.cur_reload_time += clock.get_time()/1000
            else:
                self.cur_reload_time = 0
                self.reloading = False


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
        position = Vector2((player1.rect.x - self.rect.x),(player1.rect.y - self.rect.y)).normalize()
        self.rect.x += position.x*10
        self.rect.y += position.y*10

        


class bullet(Gamesprite):
    def __init__(self,player_x,player_y,player_image,player_speed,size_x,size_y):
        super().__init__(player_x,player_y,player_image,player_speed,size_x,size_y)
        self.fier_position = Vector2( mouse.get_pos()[0] - player_x, mouse.get_pos()[1] - player_y).normalize()



    def update(self):
        if self.rect.x > 0 and self.rect.x < 1000 and self.rect.y > 0 and self.rect.y < 1000:
            self.rect.x += self.fier_position.x*10
            self.rect.y += self.fier_position.y*10
        else:
            self.kill()

class boss(Gamesprite):
    def __init__(self,player_x,player_y,player_image,player_speed,size_x,size_y):
        super().__init__(player_x,player_y,player_image,player_speed,size_x,size_y)
        self.hp = 100
        self.move = True
        self.right_move = 1
    def update(self):
        if self.rect.x < 715 and move == True and self.right_move == 1:
            self.rect.x += 5
        if self.rect.x >= 715 and self.right_move == 1:
            self.right_move = 0
        if self.rect.x > -15 and move == True and self.right_move == 0:
            self.rect.x -= 5
        if self.rect.x <= -15 and self.right_move == 0:
            self.right_move = 1



            

bullets = sprite.Group()        
global enemy1
global enemy2
global enemy3
enemy1 = enemy(randint(100,200),randint(100,200),'angry.jpg',5,50,50)
enemy2 = enemy(randint(300,400),randint(100,200),'angry.jpg',5,50,50)
enemy3 = enemy(randint(600,700),randint(100,200),'angry.jpg',5,50,50)    
enemys = sprite.Group()
enemys.add(enemy1)
enemys.add(enemy2)  
enemys.add(enemy3)


window = display.set_mode((1000,1000),flags = RESIZABLE)
display.set_caption('догонялки')
background = transform.scale(image.load('game_fone.webp'),(1000,1000))

global player1
player1 = player(500,900,'faicet_higets_lvl.webp',15,50,50)
players = sprite.Group()
players.add(player1)



global portal
portal = Gamesprite(350,0,"portal.webp",0,300,200)
boss_spawn = 0
kd = 100
laser_num = 0
win_num = 20
remove = 1
enemys_update = False
game = True
lasers_update = False
boss_update = False

while game:
    window.blit(background,(0,0))
    clock.tick(FPS)
    if win_num >= 20:
        portal.update()
        portal.reset()
    player1.update()
    player1.reset()
    bullets.draw(window)
    bullets.update()
    player1.fire()
    '''if kd >= 100 and laser_num < 3 and lasers_update == True:
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
        wall2.reset()'''

    if enemys_update == True:
        enemys.draw(window)
        enemys.update()


    if lasers_update == True:
        if sprite.collide_rect(player1,wall1) or sprite.collide_rect(player1,wall2):
            game = False
    if enemys_update == True:        
        if sprite.groupcollide(players,enemys,True,True):
            game = False

    if boss_update == True:
        boss1.update()
        boss1.reset()


    if sprite.collide_rect(player1,portal) and win_num >= 20 and boss_spawn < 1:
        player1.rect.x = 500
        player1.rect.y = 900
        enemys_update = True
        enemy1.rect.x = randint(100,200)
        enemy1.rect.y = 0
        enemy2.rect.x = randint(400,500)
        enemy2.rect.y = 0
        enemy3.rect.x = randint(700,800)
        enemy3.rect.y = 0
        win_num = 0
        boss_spawn += 1
    
    if sprite.collide_rect(player1,portal) and win_num >= 20 and boss_spawn >= 1:
        player1.rect.x = 500
        player1.rect.y = 900
        boss1 = boss(350,0,'boss1_imagen2.webp',5,300,200)
        boss_update = True
        win_num = 0


    if sprite.groupcollide(enemys,bullets,True,True):        
        vrag = enemy(randint(100,900),0,'angry.jpg',5,65,65)
        enemys.add(vrag)
        win_num += 1



    if win_num == 20:
        enemys_update = False



    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()    


