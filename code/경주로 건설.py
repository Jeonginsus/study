def solution(board):
    b_len = len(board)
    answer = 0
    que = list()
    test_list = list(list([99999999999]*b_len) for _ in range(b_len))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    que.append([0, 0, -1])
    test_list[0][0] = 0
    while que:
        ro, co, direc = que.pop(0)
        if direc == -1:
            for a in range(4):
                row = ro + dr[a]
                col = co + dc[a]
                if 0 <= row < b_len and 0 <= col < b_len and board[row][col] == 0 and test_list[row][col] >= test_list[ro][co]+100:
                    test_list[row][col] = test_list[ro][co]+100
                    que.append([row, col, a])
        else:
            for a in range(4):
                row = ro + dr[(direc + a)%4]
                col = co + dc[(direc + a)%4]
                if 0 <= row < b_len and 0 <= col < b_len and board[row][col] == 0:
                    if a == 0 and test_list[row][col] >= test_list[ro][co]+100:
                        test_list[row][col] = test_list[ro][co]+100
                        que.append([row, col, (direc + a)%4])
                    elif (a == 1 or a == 3) and test_list[row][col] >= test_list[ro][co]+600:
                        test_list[row][col] = test_list[ro][co]+600
                        que.append([row, col, (direc + a)%4])
    answer = test_list[b_len-1][b_len-1]
    return answer
    