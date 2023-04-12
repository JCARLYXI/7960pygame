import sys
from initData import *

pygame.init()

pygame.display.set_caption('线条小狗冲冲冲')
iconImg = pygame.image.load('images/logo.png')
pygame.display.set_icon(iconImg)

screen = pygame.display.set_mode((750, 500))

clock = pygame.time.Clock()

gameState = 'GAMEREADY'

score = 0

readyImgRect = None
gameoverImgRect = None

ADDBARRIER = 101

ANIMATION = 102

JUMP = 103

click_sound = pygame.mixer.Sound('click.wav')
pick_up_sound = pygame.mixer.Sound('bark.wav')
fail_sound = pygame.mixer.Sound('fail.wav')

pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(-1, 0.0)

setRandXY_bone1()
setRandXY_bone2()


def draw():
    global readyImgRect,gameoverImgRect
    screen.blit(bg['img'], (bg['x'], bg['y']))
    screen.blit(bg['img'], (bg['x'] + 750, bg['y']))
    screen.blit(gd['img'], (gd['x'], gd['y']))
    screen.blit(gd['img'], (gd['x'] + 750, gd['y']))
    screen.blit(player['img'], (player['x'], player['y']))
    screen.blit(bone1['img'], [bone1['x'], bone1['y']])
    screen.blit(bone2['img'], [bone2['x'], bone2['y']])
    
    for barrier in barrierList:
        screen.blit(barrier['img'], [barrier['x'], barrier['y']])
    if gameState == 'GAMEREADY':
        readyImgRect = readyImg.get_rect()
        readyImgRect.center = screen.get_rect().center
        screen.blit(readyImg, (readyImgRect.x, readyImgRect.y))
    elif gameState == 'GAMEOVER':
        gameoverImgRect = gameoverImg.get_rect()
        gameoverImgRect.center = screen.get_rect().center
        screen.blit(gameoverImg, (gameoverImgRect.x, gameoverImgRect.y))
        
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(score), True, (20,23,34))
        textRect = text.get_rect()
        textRect.center = screen.get_rect().center
        screen.blit(text, (textRect.x, textRect.y))
    elif gameState == 'RUNNING':
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('SCORE: '+str(score), True, (20,23,34))
        screen.blit(text, (620, 20))

def move():
    global barrierList
    bg['x'] -= bg['step']
    if bg['x'] <= -750:
        bg['x'] = 0
    gd['x'] -= gd['step']
    if gd['x'] <= -750:
        gd['x'] = 0
    new_barrierList = []
    for barrier in barrierList:
        barrier['x'] -= barrier['step']
        if barrier['x'] > -barrier['width']:
            new_barrierList.append(barrier)
    barrierList = new_barrierList
    bone1['x'] -= bone1['step']
    bone2['x'] -= bone2['step']
    if bone1['x'] < -bone1['width']:
        setRandXY_bone1()
    if bone2['x'] < -bone2['width']:
        setRandXY_bone2()


def jumpY():
    player['y'] -= player['stepy']
    if player['y'] <= player['jumpMax']:
        player['stepy'] = -3
    if player['y'] >= player['jumpBegin']:
        
        pygame.time.set_timer(JUMP, 0)
        player['y'] = player['jumpBegin']
        player['state'] = 'running'

def checkHit(p, b):
    top = b['y'] - p['height']
    bottom = b['y'] + b['height']
    left = b['x'] - p['width']
    right = b['x'] + b['width']
    if p['x'] >= left and p['x'] <= right:
        if p['y'] >= top and p['y'] <= bottom:
            return True

def check():
    global score
    global gameState
    for barrier in barrierList:
        if checkHit(player, barrier):
            gameState = 'GAMEOVER'
            fail_sound.play()
            player['img'] = failImg  
            break
        else:
            if player['x'] > barrier['x'] + barrier['width']:
                if barrier['isScored'] == False:
                    score += 10
                    barrier['isScored'] = True
    if checkHit(player, bone1):
        score += 100
        pick_up_sound.play()
        setRandXY_bone1()
    if checkHit(player, bone2):
        score += 200
        pick_up_sound.play()
        setRandXY_bone2()

def checkPoint(objRect, pos):
    top = objRect.y
    bottom = objRect.y + objRect.height
    left = objRect.x
    right = objRect.x + objRect.width
    if pos[0]>=left and pos[0] <= right:
        if pos[1] >= top and pos[1] <= bottom:
            return True

def eventListen():
    global gameState
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == ADDBARRIER:
            if gameState == 'RUNNING':
                barrierList.append(getBarrier())
        elif event.type == ANIMATION and player['state']=='running':
            animation()
        elif event.type == JUMP:
            jumpY()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player['state'] == 'running':
                    player['stepy'] = 3
                    pygame.time.set_timer(JUMP, 10)
                player['state'] = 'jumping'
                player['img'] = playerImgList[3]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == 'GAMEREADY':
                pos = pygame.mouse.get_pos()
                click_sound.play()
                if checkPoint(readyImgRect, pos):
                    gameState = 'RUNNING'
                    pygame.time.set_timer(ADDBARRIER, 1500)
                    pygame.time.set_timer(ANIMATION, 100)
            elif gameState == 'GAMEOVER':
                pos = pygame.mouse.get_pos()
                if checkPoint(gameoverImgRect, pos):
                    gameState = 'RUNNING'
                   
                    pygame.time.set_timer(ADDBARRIER, 1500)
                    pygame.time.set_timer(ANIMATION, 30)
                    resetData()

def resetData():
    global barrierList, score
    bg['x'] = 0
    bg['y'] = 0
    gd['x'] = 0
    gd['y'] = 330
    player['x'] = 80
    player['y'] = 330 - playerRect.height
    player['state'] = 'running'
    setRandXY_bone1()
    setRandXY_bone2()
    barrierList = []
    score = 0

def animation():
    player['index'] += 1
    if player['index'] >= 14:
        player['index'] = 0
    player['img'] = playerImgList[player['index']]


def stopTimer():
    pygame.time.set_timer(ADDBARRIER, 0)
    pygame.time.set_timer(ANIMATION, 0)
    pygame.time.set_timer(JUMP, 0)

while True:
    clock.tick(60)
    eventListen()
    draw()
    if gameState == 'RUNNING':
        move()
        check()
    elif gameState == 'GAMEOVER':
        stopTimer()
    pygame.display.update()

