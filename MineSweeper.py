import math
import random
from collections import deque
import os

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dx1 = [-1,1,0,0,-1,-1,1,1]
dy1 = [0,0,-1,1,-1,1,-1,1]

mineMap = [[0]*7 for _ in range(7)]
checkMap = [[False]*7 for _ in range(7)]


total_mine = 8
count = 0

#지뢰찾기를 위해 주변 1칸의 지뢰정보를 기록
def bfs(x, y):
    queue = deque()
    visit = [[0]*7 for _ in range(7)]
    queue.append((x, y))
    
    while queue:
        os.system('cls')
        for i in mineMap:
            print(i)
        x,y = queue.popleft()
        visit[x][y] = 1

        for i in range(8):
            nx = x+dx1[i]
            ny = y+dy1[i]

            if(0<=nx<7 and 0<=ny<7 and visit[nx][ny]==0):
                if(mineMap[nx][ny]!= -1 and mineMap[x][y]== -1):
                    mineMap[nx][ny] += 1
                    visit[nx][ny] = 1
                    queue.append((nx, ny))

#한 점을 눌렀을때에 누른 점이 주변에 지뢰가 존재하지 않는 점일 경우, 주변 지뢰가 있는 부분까지 확장됨
def game(x, y):
    queue = deque()
    visit = [[0]*7 for _ in range(7)]
    queue.append((x, y))
    
    while queue:
        
        x,y = queue.popleft()
        visit[x][y] = 1

        for i in range(8):
            nx = x+dx1[i]
            ny = y+dy1[i]

            if(0<=nx<7 and 0<=ny<7 and visit[nx][ny]==0):
                if(mineMap[nx][ny]== 0):
                    checkMap[nx][ny] = True
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                if(mineMap[nx][ny] > 0):
                    checkMap[nx][ny] = True
                    visit[nx][ny] = 1
                

# 지뢰배치
while True:
     if count ==  total_mine:
         break

     x = random.randrange(0,7)
     y = random.randrange(0,7)

     # 마인배치
     if mineMap[x][y] != -1:
        mineMap[x][y] = -1
        count+=1

for i in range(7):
    for j in range(7):
        if mineMap[i][j] == -1:
            bfs(i, j)


while True:
    os.system('cls')
    for i in checkMap:
        print(i)
    print('클릭할 좌표 : ',end='')
    x,y = map(int,input().split())
    if(mineMap[x][y] == -1):
        print('Fail')
        break
    elif(mineMap[x][y]== 0):
        game(x, y)
    else:
        checkMap[x][y] = True
