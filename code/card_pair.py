from collections import deque

answer = 500
def DFS(r, c, test_list, count, vis_list, num_loc, max_card, nn):
    global answer
    if answer <= count+((max_card-nn)*4)-1:
        return
    for a in range(max_card):
        if vis_list[a] == 1:
            vis_list[a] = 0
            now_loc = num_loc[a]
            for n in range(2):
                num = 2
                if n == 0:
                    move_list = BFS(r, c, test_list)
                    num += move_list[now_loc[0][0]][now_loc[0][1]]
                    test_list[now_loc[0][0]][now_loc[0][1]] = 0
                    move_list = BFS(now_loc[0][0], now_loc[0][1], test_list)
                    num += move_list[now_loc[1][0]][now_loc[1][1]]
                    test_list[now_loc[1][0]][now_loc[1][1]] = 0
                    count += num
                    if sum(vis_list) == 0:
                        answer = min(count, answer)
                    DFS(now_loc[1][0], now_loc[1][1], test_list, count, vis_list, num_loc, max_card, nn+1)  
                else:
                    move_list = BFS(r, c, test_list)
                    num += move_list[now_loc[1][0]][now_loc[1][1]]
                    test_list[now_loc[1][0]][now_loc[1][1]] = 0
                    move_list = BFS(now_loc[1][0], now_loc[1][1], test_list)
                    num += move_list[now_loc[0][0]][now_loc[0][1]]
                    test_list[now_loc[0][0]][now_loc[0][1]] = 0
                    count += num
                    if sum(vis_list) == 0:
                        answer = min(count, answer)
                    DFS(now_loc[0][0], now_loc[0][1], test_list, count, vis_list, num_loc, max_card, nn+1)
                count -= num
                test_list[now_loc[0][0]][now_loc[0][1]] = a+1
                test_list[now_loc[1][0]][now_loc[1][1]] = a+1
            vis_list[a] = 1
            
def BFS(r, c, card_list):
    deq = deque([(r, c)])
    curr_move = list(list([-1]*4) for _ in range(4))
    curr_move[r][c] = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while deq:
        ro, co = deq.popleft()
        for a in range(4):
            row = ro + dr[a]
            col = co + dc[a]
            if 0 <= row < 4 and 0 <= col < 4 and curr_move[row][col] == -1:
                curr_move[row][col] = curr_move[ro][co] + 1
                deq.append((row, col))
        for a in range(4):
            for n in range(1, 5):
                row = ro + dr[a]*n
                col = co + dc[a]*n
                if 0 <= row < 4 and 0 <= col < 4:
                    if card_list[row][col]:
                        if curr_move[row][col] == -1:
                            curr_move[row][col] = curr_move[ro][co] + 1
                            deq.append((row, col))
                        break
                else:
                    if curr_move[row-dr[a]][col-dc[a]] == -1:
                        curr_move[row-dr[a]][col-dc[a]] = curr_move[ro][co] + 1
                        deq.append((row-dr[a], col-dc[a]))
                    break
    return curr_move
def solution(board, r, c):
    global answer
    max_card = max(max(board))
    num_loc = list(list([]) for _ in range(max_card))
    for ro in range(4):
        for co in range(4):
            if board[ro][co] != 0:
                num_loc[board[ro][co]-1].append([ro, co])
    DFS(r, c, board, 0, [1]*max_card, num_loc, max_card, 0)
    return answer