from collections import deque
import sys

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

if __name__ == "__main__" :
    answer = 0
    N = int(input())
    K = int(input())
    time = 0

    board = [[-1] * (N+2)]
    for _ in range(N) :
        board.append([-1] + [0] * N + [-1])
    board += [[-1] * (N+2)]

    for _ in range(K) :
        x, y = map(int, input().split())
        board[x][y] = 1
    
    move = []
    L = int(input())
    for _ in range(L) :
        move.append(input().split())
    
    snake = deque()
    snake.append((1, 1))
    d = 1
    x, y = 1, 1
    for i in move :
        X, C = i
        X = int(X)
        for _ in range(X - time) :
            answer += 1
            next_x, next_y = x + direction[d][0], y + direction[d][1]
            if (next_x, next_y) in snake :
                print(answer)
                sys.exit()

            if board[next_x][next_y] == -1 :
                print(answer)
                sys.exit()
            elif board[next_x][next_y] == 1 :
                board[next_x][next_y] = 0
                snake.append((next_x, next_y))
                x, y = next_x, next_y
            else :
                snake.append((next_x, next_y))
                snake.popleft()
                x, y = next_x, next_y
        time = X

        if C == "L" :
            d = (d-1)%4
        else :
            d = (d+1)%4
    
    while True :
        answer += 1
        next_x, next_y = x + direction[d][0], y + direction[d][1]
        if (next_x, next_y) in snake :
            print(answer)
            sys.exit()

        if board[next_x][next_y] == -1 :
            print(answer)
            sys.exit()
        elif board[next_x][next_y] == 1 :
            board[next_x][next_y] = 0
            snake.append((next_x, next_y))
            x, y = next_x, next_y
        else :
            snake.append((next_x, next_y))
            snake.popleft()
            x, y = next_x, next_y     
