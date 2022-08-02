def rotate(k_list):
    kn = len(k_list)
    new_list = list([0]*kn for _ in range(kn))
    for r in range(kn):
        for c in range(kn):
            new_list[r][c] = k_list[c][kn-r-1]
    return new_list

def solution(key, lock):
    answer = True
    kn = len(key)
    ln = len(lock)
    a = 0
    for r in range(ln):
        for c in range(ln):
            a += lock[r][c]
    sum_ans = ln*ln - a
    flag = False
    for _ in range(4):
        key = rotate(key)
        for rp in range(-ln+1, ln):
            for cp in range(-ln+1, ln):
                sa = 0
                for r in range(kn):
                    for c in range(kn):
                        if key[r][c] == 1:
                            if 0 <= rp+r < ln and 0 <= cp+c < ln: 
                                if lock[rp+r][cp+c] == 0:
                                    sa += 1
                                elif lock[rp+r][cp+c] == 1:
                                    sa -= 1
                if sa == sum_ans:
                    flag = True
                if flag:
                    break
            if flag:
                break    
        if flag:
            break    
    answer = flag               
    return answer