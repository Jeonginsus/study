def solution(arrows):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    rp, cp = 0, 0
    mar, mir, mac, mic = 0, 0, 0, 0 
    for ar in arrows:
        if ar == 0:
            rp -= 1
            mir = min(mir, rp)
        elif ar == 1:
            rp -= 1
            mir = min(mir, rp)
            cp += 1
            mac = max(mac, cp)
        elif ar == 2:
            cp += 1
            mac = max(mac, cp)
        elif ar == 3:
            cp += 1
            mac = max(mac, cp)
            rp += 1
            mar = max(mar, rp)
        elif ar == 4:
            rp += 1
            mar = max(mar, rp)
        elif ar == 5:
            rp += 1
            mar = max(mar, rp)
            cp -= 1
            mic = min(mic, cp)
        elif ar == 6:
            cp -= 1
            mic = min(mic, cp)
        elif ar == 7:
            cp -= 1
            mic = min(mic, cp)
            rp -= 1
            mir = min(mir, rp)
            
    answer = 0
    test_list = list([0]*(4*(mac-mic+1)) for _ in range(4*(mar-mir+1)))
    s_p = [-4*mir+1, -4*mic+1]
    test_list[s_p[0]][s_p[1]] = -1
    
    for arrow in arrows:
        flag = False
        r, c = s_p
        drr = dr[arrow]
        dcc = dc[arrow]
        for _ in range(4):
            r += drr
            c += dcc
            if test_list[r][c] == 0:
                test_list[r][c] = -1
                flag = True
            elif test_list[r][c] == -1:
                if flag:
                    answer += 1
        s_p = [r, c]
    
    return answer