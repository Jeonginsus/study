def is_check(mid, k, num, links, vis_list):
    s_p = 0
    count = 0
    while True:
        if count >= k : # 실패
            return False
        
        if vis_list[s_p] != -1: #가장아래면 위로
            if len(links[s_p]) == 2:
                return True
            s_p = links[s_p][2]
            continue
            
        if vis_list[links[s_p][0]] == -1:#왼쪽아래로
            s_p = links[s_p][0]
            continue
        if vis_list[links[s_p][1]] == -1:#오른쪽아래로
            s_p = links[s_p][1]
            continue
            
        if vis_list[links[s_p][1]]+vis_list[links[s_p][0]]+num[s_p] <= mid:#조사한노드중가장아래
            vis_list[s_p] = vis_list[links[s_p][1]]+vis_list[links[s_p][0]]+num[s_p]

        else:
            ln = num[s_p] + vis_list[links[s_p][0]]
            rn = num[s_p] + vis_list[links[s_p][1]]
            if min(rn, ln) > mid:
                count += 2
                vis_list[s_p] = num[s_p]
            else:
                count += 1
                vis_list[s_p] = min(rn, ln)
            if count >= k :
                return False
            
        if len(links[s_p]) == 2:#위가 없을때
                return True
        s_p = links[s_p][2]
        
def solution(k, num, links):
    answer = 0
    inter_links = [[] for _ in range(len(links))]
    left = max(sum(num)//k, max(num))
    mid = 0
    right = sum(num)
    vis_list = [-1]*len(num)+[0]
    for li in range(len(links)):
        if links[li] == [-1, -1]:
            vis_list[li] = num[li]
        for l in links[li]:
            if l != -1:
                inter_links[l].append(li)
        inter_links[li] = links[li]+inter_links[li]
    
    while True:
        if mid == (left+right)//2:
            if not is_check(mid, k, num, inter_links, vis_list[:]):
                mid+=1
            break
        mid = (left+right)//2
        if is_check(mid, k, num, inter_links, vis_list[:]):
            right = mid
        else:
            left = mid
    
    return mid