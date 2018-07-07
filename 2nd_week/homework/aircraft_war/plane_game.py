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

# 全局的设置类
class Settings():

    def __init__(self):
        # 定义游戏窗口大小，为背景图片的一半
        self.screen_size = (self.screen_width, self.screen_height) = (512, 768)
        self.bg_color = (230, 230, 230)
        self.bg_image = './images/bg2.jpg'
        self.gameover_image = './images/gameover.jpg'
        self.title = '飞机大战'

        # 英雄机参数
        self.move_step = 5 # 键盘控制的速度
        self.hero_style = './images/me.png'

        # 敌机参数
        self.enemy_speed = 4 # 敌机飞行速度
        self.enemy_style_list = ['./images/e0.png', './images/e1.png', './images/e2.png']

        # 子弹参数
        self.bullet_style = './images/pd.png'
        self.bullet_hero_v = 10 # 英雄机子弹速度
        self.bullet_enemy_v = 8 # 敌机子弹速度


# 实例化设置对象
settings = Settings()


# 子弹基类
class Bullet:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(settings.bullet_style)

    def __del__(self):
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        return True


# 英雄子弹类
class HeroBullet(Bullet):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    def move(self):
        self.y -= settings.bullet_hero_v
        # 判断子弹是否出界
        if self.y <= -20:
            return True


# 敌机子弹类
class EnemyBullet(Bullet):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

    def move(self):
        self.y += settings.bullet_enemy_v
        # 判断子弹是否出界
        if self.y >= settings.screen_height:
            return True


# 飞机基类
class Plane:
    def __init__(self, screen, style, geo):
        self.screen = screen
        self.image = pygame.image.load(style)
        self.bullet_list = []
        self.x = geo[0]
        self.y = geo[1]
        self.is_dead = False
        self.finished = False
        self.bomb_seq = ['4','4','3','3','2','2','1','1']

    def __del__(self):
        pass

    def display(self):
        for b in self.bullet_list:
            b.display()
            # 回收子弹
            if b.move(): self.bullet_list.remove(b)

        # 爆炸效果
        if self.is_dead:
            death_x = self.x
            death_y = self.y
            death_w = self.image.get_width()
            death_h = self.image.get_height()
            try:
                bomb_image = './images/bomb'+self.bomb_seq.pop()+'.png'
                self.image = pygame.image.load(bomb_image)
            except:
                self.image = pygame.image.load('./images/bomb4.png')
                self.finished = True
            finally:
                x = death_x + (death_w - self.image.get_width())/2
                y = death_y + (death_h - self.image.get_height())/2
                self.screen.blit(self.image, (x, y))

        else:
            # 重新绘制飞机
            self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
        print(len(self.bullet_list))

    def over(self):
        #print("Oops: plane over ...")
        #del self
        return self.finished


class HeroPlane(Plane):
    def __init__(self, screen):
        # 英雄机初始位置
        geo = (200, 600)
        super().__init__(screen, settings.hero_style, geo)

        self.step = settings.move_step
        # 英雄机移动范围
        self.limit_left = -(self.image.get_width()/2)+10
        self.limit_right = settings.screen_width-self.image.get_width()/2-10
        self.limit_top = 5
        self.limit_bottom = settings.screen_height-self.image.get_height()

    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen, self.x+53, self.y))

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


class EnemyPlane(Plane):
    def __init__(self, screen):
        geo = (random.choice(range(408)), -75)
        enemy_style = settings.enemy_style_list[random.choice(range(3))]
        super().__init__(screen, enemy_style, geo)

        self.pipe_x = self.image.get_width()/2-1 # 1 for the width of bullet
        self.pipe_y = self.image.get_height()

    def move(self, hero):
        self.y += settings.enemy_speed
        if self.y > settings.screen_height:
            return True

        # 碰撞检测
        if self.x > hero.x-50 and self.x < hero.x+50 and self.y > hero.y-40 and self.y < hero.y+40:
            self.is_dead = True
            hero.is_dead = True

        # 看看我中弹了没
        for bo in hero.bullet_list:
            if bo.x > self.x+12 and bo.x < self.x+92 and bo.y < self.y+60:
                hero.bullet_list.remove(bo)
                # 爆炸
                self.is_dead = True

        # 看看英雄机中弹了没
        for bo in self.bullet_list:
            if bo.x > hero.x+25 and bo.x < hero.x+75 and bo.y > hero.y+5 and bo.y < hero.y+50:
                self.bullet_list.remove(bo)
                hero.is_dead = True

    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen, self.x+self.pipe_x, self.y+self.pipe_y))


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

    # 初始化 Pygame
    pygame.init()

    # 创建一个游戏窗口
    screen = pygame.display.set_mode(settings.screen_size, 0, 0)

    # 设置窗口标题
    pygame.display.set_caption(settings.title)

    # 在窗口中加载游戏背景
    background = pygame.image.load(settings.bg_image)

    # 创建英雄机
    hero = HeroPlane(screen)

    play = True
    enemylist = []
    bg_y = -(settings.screen_height)

    while True:
        # 从坐标(0, -768)开始绘图，所以看到的是背景图片的下半部
        screen.blit(background, (0, bg_y))
        bg_y += 2
        if bg_y >= 0:
            bg_y = -(settings.screen_height)

        if play:

            # 绘制英雄机
            hero.display()

            # 随机绘制敌机
            if random.choice(range(50)) == 10:
                enemylist.append(EnemyPlane(screen))

            # 遍历敌机并绘制移动
            for em in enemylist:
                em.display()

                # 敌机随机发炮弹
                if random.choice(range(50)) == 10:
                    em.fire()

                # 判断敌机是否出界
                if em.move(hero):
                    enemylist.remove(em)
                # 判断敌机是否炸毁
                if em.over():
                    enemylist.remove(em)

            # 英雄机炸毁，游戏结束
            if hero.over():
                play = False

            #pygame.display.flip()
            pygame.display.update()

        else:
            gameover = pygame.image.load(settings.gameover_image)
            screen.blit(gameover, ((settings.screen_width-gameover.get_width())/2,
                        (settings.screen_height-gameover.get_height())/2))
            pygame.display.update()
            #print("Game Over")
            #continue

        # 检查按键事件
        check_event(hero)

        time.sleep(0.04)



# 判断是否为主运行程序，是则调用 main()
if __name__ == '__main__':
    main()

