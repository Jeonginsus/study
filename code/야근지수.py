def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    now_p = 0
    flag = True
    counting = 0
    while flag:
        for a in range(now_p+1):
            if works[a] == 0:
                flag = False
                break
            works[a]-=1
            counting += 1
            if counting == n:
                flag = False
                break
        else:
            while True:
                if now_p+1 < len(works) and works[now_p] < works[now_p+1]:
                    now_p += 1
                    if works[now_p] == 0:
                        flag = False
                        break
                    works[now_p] -= 1
                    counting += 1
                    if counting == n:
                        flag = False
                        break
                else:
                    break
    for w in works:
        answer += w**2
    return answer