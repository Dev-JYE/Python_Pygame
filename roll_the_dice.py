import random
def board():
    print('*'*(player-1)+'☆'+'*'*(30-player)+' GOAL')
    print('*'*(com-1)+'◇'+'*'*(30-com)+' GOAL')
player=1
com=1
while True:
    board()
    input('Enter를 누르면 당신의 말이 움직입니다.')
    player+=random.randint(1,6)
    if player>30:
        player=30
    board()
    if player==30:
        print('YOU WIN!')
        break
    input('Enter를 누르면 컴퓨터의 말이 움직입니다.')
    com+=random.randint(1,6)
    if com>30:
        com=30
    if com==30:
        print('YOU LOSE ㅠ ㅠ')
        break







