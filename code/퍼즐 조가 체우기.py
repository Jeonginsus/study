def solution(game_board, table):
    answer = 0
    mark = 1
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    R = len(game_board)
    
    for i in range(R):
        for j in range(R):
            if game_board[i][j] == 0:
                mark += 1
                game_board[i][j] = mark
                que = [[i, j]]
                while que:
                    r, c = que.pop(0)
                    for a in range(4):
                        ro = r+dr[a]
                        co = c+dc[a]
                        if 0<=ro<R and 0<=co<R:
                            if game_board[ro][co] == 0:
                                game_board[ro][co] = mark
                                que.append([ro, co])
                                
    mark = 1
    for i in range(R):
        for j in range(R):
            if table[i][j] == 1:
                mark += 1
                table[i][j] = mark
                que = [[i, j]]
                while que:
                    r, c = que.pop(0)
                    for a in range(4):
                        ro = r+dr[a]
                        co = c+dc[a]
                        if 0<=ro<R and 0<=co<R:
                            if table[ro][co] == 1:
                                table[ro][co] = mark
                                que.append([ro, co])
                                
    max_num_e = max(map(max, game_board))
    max_num_b = max(map(max, table))
    total_empty_area = list([] for _ in range(max_num_e+1))
    vis_list = [False]*(max_num_e+1)
    empty_area = list([] for _ in range(max_num_e+1))
    block_area = list([] for _ in range(max_num_b+1))
    
    for i in range(R):
        for j in range(R):
            if table[i][j] > 1:
                block_area[table[i][j]].append([i, j])
                
    for i in range(R):
        for j in range(R):
            if game_board[i][j] > 1:
                empty_area[game_board[i][j]].append([i, j])
    
    for en in range(len(empty_area)):
        if en <= 1:
            continue
            
        for _ in range(4):
            
            num_list = []
            min_r = 99999
            min_c = 99999
            
            for e in range(len(empty_area[en])):
                min_r = min(min_r, 5-empty_area[en][e][1])
                min_c = min(min_c, empty_area[en][e][0])
                empty_area[en][e] = [5-empty_area[en][e][1], empty_area[en][e][0]]
                
            _cost = 6*min_r +min_c
            
            for er, ec in empty_area[en]:
                num_list.append(6*er+ec - _cost)
                
            num_list.sort()
            
            total_empty_area[en].append(num_list[:])
   
    for bn in range(len(block_area)):
        if bn <= 1:
            continue
        
        num_list = []
        min_r = 99999
        min_c = 99999
        
        for br, bc in block_area[bn]:
            min_r = min(min_r, br)
            min_c = min(min_c, bc)
            
        _cost = 6*min_r +min_c
        
        for br, bc in block_area[bn]:
            num_list.append(6*br+bc - _cost)
            
        num_list.sort()
        
        for tea in range(len(total_empty_area)):
            if not vis_list[tea] and num_list in total_empty_area[tea]:
                vis_list[tea] = True
                answer += len(num_list)
                break        
                              
    return answer