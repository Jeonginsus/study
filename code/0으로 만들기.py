import sys
sys.setrecursionlimit(300000)
vis_list = []
answer = 0

def DFS(a, line_list, _start):
    global answer, vis_list
    vis_list[_start] = False
    _total_value = a[_start]
    for _next in line_list[_start]:
        if vis_list[_next]:
            _value = DFS(a, line_list, _next)
            _total_value += _value
    answer += abs(_total_value)
    return _total_value

def solution(a, edges):
    global vis_list, answer
    if sum(a) != 0:
        answer = -1
    else:
        vis_list = [True]*len(a)
        line_list = [[] for _ in range(len(a))]
        for (e1, e2) in edges:
            line_list[e1].append(e2)
            line_list[e2].append(e1)
        DFS(a, line_list, 0)  
    return answer