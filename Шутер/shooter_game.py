from pygame import *
from random import *
from time import time as timer


win_width = 700
win_height = 500
display.set_caption('БИТВА ВСЕЛЕННОЙ!!!!!')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

'''music'''
mixer.init()
mixer.music.load('x2downloadapp-insight-320-kbps_SDGrHYXh.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

'''fonts'''
font.init()
font1 = font.SysFont(None, 80)
win = font1.render('Thanks For Playing!', True, (255, 255, 255))
lose = font1.render('LOSE', True, (255, 255, 255))
font2 = font.SysFont(None, 36)

'''Game'''
score = 0  #ships killed
lost = 0  #ships missed
max_lost = 3  #lost when missed 3 ships
goal = 30  #ships need to kill to win
life = 3 #health

class GameSprite(sprite.Sprite):
    '''the parent of other sprites'''
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        '''every sprite keeps an image'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        '''every sprite is a rectangle'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        '''appearance of sprite on screen'''
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    '''Class of main player'''
    def update(self):
        '''method of sprite controlling'''
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        '''shooting'''
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15,)
        bullets.add(bullet)

class Enemy(GameSprite):
    '''enemy class'''
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

class Asteroid(GameSprite):
    '''asteroid class'''
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(30, win_width - 30)
            self.rect.y = 0


class Bullet(GameSprite):
    '''Class of bullets'''
    def update(self):
        '''movement of bullet'''
        self.rect.y += self.speed
        '''disappears when goes out of the screen'''
        if self.rect.y < 0:
            self.kill()



'''creating sprites'''
ship = Player('rocket.png',5,win_height - 100,80,100,15)
monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)


asteroids = sprite.Group()
for i in range(1,6):
    asteroid = Asteroid('asteroid.png', randint(30, win_width - 30), -40, 80, 50, randint(1, 3))
    asteroids.add(asteroid)

bullets = sprite.Group()

'''Game Over'''
finish = False

'''Main cycle of the game'''
run = True

num_fire = 0  #number of shoots
rel_time = False  #Reloading


while run:
    for e in event.get():
        '''Button X on window'''
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True






    if not finish:
        '''updating the back'''
        window.blit(background,(0,0))

        '''text on the screen'''
        text = font2.render('KILLED:'+str(score), 1, (255, 255, 255))
        window.blit(text, (20, 10))
        textlose = font2.render('MISSED:' + str(lost), 1, (255, 255, 255))
        window.blit(textlose, (10, 50))

        '''Movement of sprites'''
        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()
        '''Updating the location of sprites'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        '''reloading'''
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font2.render('Wait, reloading..', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False

        '''checking if bullet touches the monster'''
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        '''if player touches monsters -1 HEALTH'''

        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False) :
            sprite.spritecollide(ship, monsters,True)
            sprite.spritecollide(ship, asteroids, True)
            life -= 1

        '''Defeat'''
        if life == 0 or lost == max_lost:
            finish = True
            window.blit(lose, (200, 200))

        '''Victory'''
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(win, (200, 200))
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0 , 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))



        display.update()
    time.delay(50)



