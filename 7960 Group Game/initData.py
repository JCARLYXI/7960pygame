from loadImg import *
import random

barrierList = []

bg = {
        'img': bgImg,
        'x': 0,
        'y': 0,
        'step': 3
}

gd = {
        'img': gdImg,
        'x': 0,
        'y': 330,
        'step': 3
}

playerRect = playerImgList[0].get_rect()
player = {
        'img': playerImgList[0],
        'x': 80,
        'y': 330 - playerRect.height,
        'width': playerRect.width,
        'height': playerRect.height,
        'index': 0,
        'stepy': 3,
        'jumpMax': 330 - playerRect.height - 150,
        'jumpBegin': 330 - playerRect.height,
        'state': 'running'
}

gRect_1 = bone1.get_rect()
gRect_2 = bone2.get_rect()
bone1 = {'img': bone1,
        'x': 0,
        'y': 0,
        'width': gRect_1.width,
        'height': gRect_1.height,
        'step': 4
        }
bone2 = {'img': bone2,
        'x': 0,
        'y': 0,
        'width': gRect_2.width,
        'height': gRect_2.height,
        'step': 4
        }


def getBarrier():
    barrierImg = random.choice(barrierImgList)
    barrierRect = barrierImg.get_rect()
    barrier = {
            'img': barrierImg,
            'x': 750,
            'y': 330 - barrierRect.height,
            'width': barrierRect.width,
            'height': barrierRect.height,
            'step': 4,
            'isScored': False
    }
    return barrier


def setRandXY_bone1():
    bone1['x'] = 800
    bone1['y'] = random.randint(player['jumpMax'] - bone1['height'],
                                330 - bone1['height'])

def setRandXY_bone2():
    bone2['x'] = 1000
    bone2['y'] = random.randint(player['jumpMax'] - bone1['height'],
                                330 - bone1['height'])
