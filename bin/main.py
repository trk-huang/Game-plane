import sys
import pygame

from pygame.constants import *

from conf.setting import *
from src.plane import Plane
from src.enemy import SmallEnemyPlane
from src.bullet import Bullet

# 学习pygame 音频循环 游戏画面渲染 键盘事件处理  clock
bg_size = 480, 852
screen = pygame.display.set_mode(bg_size)  # 设置窗口的宽高
pygame.display.set_caption("Game-Plane")
bg_img = pygame.image.load(os.path.join(BASE_DIR, BG_IMG))


def add_small_enemy(enemy_groups1, enemy_groups2, num):
    for i in range(num):
        small_enemy = SmallEnemyPlane(bg_size)
        enemy_groups1.add(small_enemy)
        enemy_groups2.add(small_enemy)


def add_bullet(our_plane, bullets_group, num):
    for i in range(num):
        bullet = Bullet(our_plane.rect.midtop)
        bullets_group.append(bullet)


def main():
    pygame.mixer.music.play(-1)
    our_plane = Plane(bg_size)
    switch_image = False  # 定义飞机的切图效果标识
    delay_time = 60
    running = True

    enemies = pygame.sprite.Group()
    small_enemies = pygame.sprite.Group()
    add_small_enemy(enemies, small_enemies, 4)

    bullet_index = 0
    e1_destroy_index = 0
    plane_destroy_index = 0

    bullet1 = []
    bullet_num = 10
    add_bullet(our_plane, bullet1, bullet_num)

    while running:
        screen.blit(bg_img, (0, 0))

        clock = pygame.time.Clock()
        clock.tick(60)

        if not delay_time % 3:
            switch_image = not switch_image

        for small_enemy in small_enemies:
            if small_enemy.active:
                for e in small_enemies:
                    e.move()
                    screen.blit(e.image, e.rect)
            else:
                if e1_destroy_index == 0:
                    enemy_over_sound.play()
                screen.blit(small_enemy.destroy_images[e1_destroy_index], small_enemy.rect)
                e1_destroy_index = (e1_destroy_index + 1) % 4
                if e1_destroy_index == 0:
                    small_enemy.reset()

        if our_plane.active:
            if switch_image:
                screen.blit(our_plane.image_one, our_plane.rect)
            else:
                screen.blit(our_plane.image_two, our_plane.rect)
            if not (delay_time % 10):
                bullet_sound.play()
                bullets = bullet1
                bullets[bullet_index].reset(our_plane.rect.midtop)
                bullet_index = (bullet_index + 1) % bullet_num

            for bullet in bullets:
                if bullet.active:
                    bullet.move()
                    screen.blit(bullet.image, bullet.rect)
                    enemies_hit = pygame.sprite.spritecollide(bullet, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        bullet.active = False
                        for e in enemies_hit:
                            e.active = False
        else:
            if not (delay_time % 3):
                screen.blit(our_plane.destroy_images[plane_destroy_index], our_plane.rect)
                plane_destroy_index = (plane_destroy_index + 1) % 4
                if plane_destroy_index == 0:
                    game_over_sound.play()
                    our_plane.reset()
        plane_enemy_hit = pygame.sprite.spritecollide(our_plane, enemies, False, pygame.sprite.collide_mask)
        if plane_enemy_hit:
            our_plane.active = False
            for e in enemies:
                e.active = False
        if delay_time == 0:
            delay_time = 60
        delay_time -= 1

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            our_plane.move_left()
        elif key_pressed[K_w] or key_pressed[K_UP]:
            our_plane.move_up()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            our_plane.move_right()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            our_plane.move_down()
        if key_pressed[K_j]:
            our_plane.active = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # 再而我们将背景图像并输出到屏幕上面
        pygame.display.flip()


if __name__ == "__main__":
    main()
