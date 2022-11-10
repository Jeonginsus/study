disable_list = []
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,7,7,7,0,0,0,0,0],[0,0,0,7,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,6,0,0,5],[1,1,1,0,6,6,6,0,0,5]]
def dfs(n, link_list):
    global disable_list
    print("in dfs: ", n, link_list[n])
    for l in link_list[n]:
        if disable_list[l]:
            disable_list[l] = False
            dfs(l, link_list)
    
def solution(board):
    global disable_list
    
    m_num = max(map(max, board))+1
    
    count_list = [0]*m_num
    disable_list = [True]*m_num
    
    for bo in board:
        new_dict = {}
        for b in bo:
            if b!=0:
                if new_dict.get(b) == None:
                    new_dict[b] = 1
                else:
                    new_dict[b] += 1
        for key, val in new_dict.items():
            if val == 2 and count_list[key] != 2:
                disable_list[key] = False
            elif val == 3 and count_list[key] == 0:
                disable_list[key] = False
            print(count_list, key)
            count_list[key] += val
    
    link_list = list(set() for _ in range(m_num))
    
    for j in range(len(board)):
        line_link = set()
        for i in range(len(board)-1, -1, -1):
            n = board[i][j]
            if n != 0:
                link_list[n] = link_list[n].union(line_link)
                line_link.add(n)
        
    copy_list = disable_list[:]
    
    for a in range(1, m_num):
        if copy_list[a] == False:
            print("start")
            dfs(a, link_list)
    
    return disable_list.count(True)-1

print(solution(board))