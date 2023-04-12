import pygame

# 背景
bgImg = pygame.image.load('images/bg.png')

# 地面
gdImg = pygame.image.load('images/ground.png')

# 狗狗
playerImgList = []
for i in range(1,15):
    playerImg = pygame.image.load('images/player_run_'+str(i)+'.png')
    playerImgList.append(playerImg)

# 障碍物
barrierImgList = []
for i in range(1, 7):
    barrierImg = pygame.image.load('images/barrier' + str(i) + '.png')
    barrierImgList.append(barrierImg)


#游戏失败图片
failImg = pygame.image.load('images/player_fail.png')

#加载准备界面图片
readyImg = pygame.image.load('images/gameready.png')

#游戏结束积分牌
gameoverImg = pygame.image.load('images/gameover.png')

#骨头
bone1 = pygame.image.load('images/bone1.png')
bone2 = pygame.image.load('images/bone2.png')