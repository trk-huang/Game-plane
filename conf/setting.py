import pygame
import os

# 学习python常量开发 相对路径 pygame资源加载 初始化 混音器初始化
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BG_IMG = "res/image/background.png"
GAME_MUSIC = "res/sound/game_music.wav"
BULLET_MUSIC = "res/sound/bullet.wav"
GAME_OVER_MUSIC = "res/sound/game_over.wav"
ENEMY_OVER_MUSIC = "res/sound/enemy1_down.wav"

#游戏初始化，混音器初始化
pygame.init()
pygame.mixer.init()



#加载资源
game_sound = pygame.mixer.music.load(GAME_MUSIC)  # 背景音乐声音设置
pygame.mixer.music.set_volume(0.2)


bullet_sound = pygame.mixer.Sound(BULLET_MUSIC) # 子弹发射声音设置
bullet_sound.set_volume(0.3)

game_over_sound = pygame.mixer.Sound(GAME_OVER_MUSIC)  # 游戏结束声音设置
game_over_sound.set_volume(0.3)

enemy_over_sound = pygame.mixer.Sound(ENEMY_OVER_MUSIC) # 敌军被消灭声音设置
enemy_over_sound.set_volume(0.3)




