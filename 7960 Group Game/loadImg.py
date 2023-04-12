import pygame

bgImg = pygame.image.load('images/bg.png')

gdImg = pygame.image.load('images/ground.png')

playerImgList = []
for i in range(1,15):
    playerImg = pygame.image.load('images/player_run_'+str(i)+'.png')
    playerImgList.append(playerImg)

barrierImgList = []
for i in range(1, 7):
    barrierImg = pygame.image.load('images/barrier' + str(i) + '.png')
    barrierImgList.append(barrierImg)

failImg = pygame.image.load('images/player_fail.png')

readyImg = pygame.image.load('images/gameready.png')

gameoverImg = pygame.image.load('images/gameover.png')

bone1 = pygame.image.load('images/bone1.png')
bone2 = pygame.image.load('images/bone2.png')
