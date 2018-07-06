"""
 Name: 飞机大战
 Athor: 卢华东
 Email: luhuadong@163.com
 Date: 2018-07-06
 Description: 实现英雄机的上下左右移动和子弹发射，
              实现敌机的向下移动和子弹发射，
              实现子弹和飞机的碰撞检测，
              实现碰撞后的爆炸效果，
              增加计分功能，不同颜色的敌机分数不同，
              每局游戏，玩家都获得三架英雄飞机，
              如果敌机及其子弹碰到英雄机，玩家就会损失一架飞机
              如果敌机飞离画面下方，玩家也会损失飞机
              当玩家的三架飞机都用完时游戏介绍

              增加背景音乐
"""

import sys, time, random
import pygame
from pygame.locals import *
import threading

class Settings():

    def __init__(self):
        self.screen_width = 512
        self.screen_height = 768
        self.bg_color = (230, 230, 230)
        self.bg_image = './images/bg2.jpg'

# 定义游戏窗口大小，为背景图片的一半
size = (width, height) = (512, 768)


class Bullet:
    def __init__(self, screen, x, y):
        self.x = x+53
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('./images/pd.png')

    def __del__(self):
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10
        if self.y <= -20:
            return True

class Plane:
    def __init__(self, screen):
        pass

    def __del__(self):
        pass


class HeroPlane:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/me.png')
        self.bullet_list = []
        self.x = 200
        self.y = 600
        self.step = 5
        self.limit_left = -(self.image.get_width()/2)+10
        self.limit_right = width-self.image.get_width()/2-10
        self.limit_top = 5
        self.limit_bottom = height-self.image.get_height()

    def __del__(self):
        pass

    def display(self):

        for b in self.bullet_list:
            b.display()
            if b.move(): self.bullet_list.remove(b)

        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
        print(len(self.bullet_list))

    def move_left(self):
        if self.x <= self.limit_left:
            pass
        else:
            self.x -= self.step

    def move_right(self):
        if self.x >= self.limit_right:
            pass
        else:
            self.x += self.step

    def move_up(self):
        if self.y <= self.limit_top:
            pass
        else:
            self.y -= self.step

    def move_down(self):
        if self.y >= self.limit_bottom:
            pass
        else:
            self.y += self.step


class EnemyBullet:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('./images/pd.png')

    def __del__(self):
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 8
        if self.y >= height:
            return True


class EnemyPlane:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./images/e'+str(random.choice(range(3)))+'.png')
        self.bullet_list = []
        self.x = random.choice(range(408))
        self.y = -75
        self.pipe_x = self.image.get_width()/2
        self.pipe_y = self.image.get_height()
        self.timer = threading.Timer(1, self.fire)
        self.timer.start()

    def __del__(self):
        self.timer.cancel()

    def display(self):
        for b in self.bullet_list:
            b.display()
            if b.move(): self.bullet_list.remove(b)
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, hero):
        self.y += 4
        if self.y > height:
            return True

        for bo in hero.bullet_list:
            if bo.x > self.x+12 and bo.x < self.x+92 and bo.y < self.y+60:
                hero.bullet_list.remove(bo)
                return True

    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen, self.x+self.pipe_x, self.y+self.pipe_y))
        #self.timer.start()
        print("Come on!")
        threading.Timer(1, self.fire).start()
        print("================")
        #print(len(self.bullet_list))




def check_event(hero):
    """
        Key event capture and key_control
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit...")
            sys.exit()

    which = pygame.key.get_pressed()

    if which[K_SPACE]:
        hero.fire()
        print("Space...")

    if which[K_LEFT] or which[K_a]:
        hero.move_left()
        #print("Left...")
    elif which[K_RIGHT] or which[K_d]:
        hero.move_right()
        #print("Right...")
    elif which[K_UP] or which[K_w]:
        hero.move_up()
        #print("Up...")
    elif which[K_DOWN] or which[K_s]:
        hero.move_down()
        #print("Down...")



def main():

    # 背景图片
    background_image = './images/bg2.jpg'

    # 初始化 Pygame
    pygame.init()

    # 创建一个游戏窗口
    screen = pygame.display.set_mode(size, 0, 0)

    # 在窗口中加载游戏背景
    background = pygame.image.load(background_image)

    hero = HeroPlane(screen)

    bg_y = -(height)
    enemylist = []

    while True:
        # 从坐标(0, -768)开始绘图，所以看到的是背景图片的下半部
        screen.blit(background, (0, bg_y))
        bg_y += 2
        if bg_y >= 0:
            bg_y = -(height)

        hero.display()
        check_event(hero)

        if random.choice(range(50)) == 10:
            enemylist.append(EnemyPlane(screen))
        for em in enemylist:
            em.display()
            if em.move(hero):
                enemylist.remove(em)

        #pygame.display.flip()
        pygame.display.update()

        time.sleep(0.04)


# 判断是否为主运行程序，是则调用 main()
if __name__ == '__main__':
    main()

