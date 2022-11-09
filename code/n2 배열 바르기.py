def solution(n, left, right):
    answer = []
    rr = right//n
    lr = left//n
    rc = right%n
    lc = left%n
    flag = True
    s_p = [lr, lc]
    e_p = [rr, rc]
    while flag:
        if s_p[1] == n:
            s_p[0] += 1
            s_p[1] = 0
        if s_p == e_p:
            flag = False
        answer.append(max(s_p[0], s_p[1])+1)
        s_p[1] += 1
            
    return answer