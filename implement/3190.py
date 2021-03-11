import sys
input=sys.stdin.readline

n=int(input()) #보드의 크기

board=[[-1]*n for i in range(n)]
# print(board)

#사과의 위치
for _ in range(int(input())):
    a, b=map(int, input().split())
    board[a-1][b-1]=-4
# print(board)

#뱀의 방향 변환
#x초 뒤 l 왼쪽, d 오른쪽 90도 회전
snake_loc=[]
for _ in range(int(input())):
    a, b = input().split()
    snake_loc.append([int(a), b])
# print(snake_loc)

#동 남 서 북
#0 1 2 3
go=[[1, 0], [0, 1], [-1, 0], [0, -1]]
head, tail=[0,0], [0,0]
cur=0 #방향
time=0
board[0][0]=0
[print(i) for i in board]
print('##')
while True:
    if snake_loc and time==snake_loc[0][0]:
        if snake_loc[0][1]=='L':
            cur-=1
        else:
            cur+=1
        if cur<0:
            cur=3
        elif cur>3:
            cur=0
        snake_loc.pop(0)
    #go
    #행, 열
    head[0]+=go[cur][1]
    head[1]+=go[cur][0]

    row, col = head[0], head[1]


    #벽에 부딪힘
    #본인 한테 부딪힘
    if row>len(board)-1 or row<0 or col>len(board)-1 or col<0 or board[row][col]>=0 :
        break
    else:
        # 사과가 있으면
        if board[row][col]==-4:
            board[row][col] = time + 1
        else:
            #꼬리 줄이기
            #오른쪽부터 보기
            # 동 남 서 북
            # 0 1 2 3
            # go = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            board[row][col] = time + 1
            k = 0
            t_row = tail[0]
            t_col = tail[1]
            while True:
                t_row_next=t_row+go[k][1]
                t_col_next=t_col+go[k][0]
                if len(board)>t_row_next>=0 and len(board)>t_col_next>=0 and board[t_row][t_col]+1==board[t_row_next][t_col_next]:
                    board[t_row][t_col]=-1
                    tail[0]= t_row_next
                    tail[1]= t_col_next
                    break
                k+=1
                if k > 3:
                    k=0


    time += 1
    print('##')
    [print(i) for i in board]
#게임이 몇 초 후에 끝나는지 출력
print(time+1)
