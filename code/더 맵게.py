import heapq

def solution(scoville, K):
    answer = 0
    test_list = []
    for i in scoville:
        heapq.heappush(test_list, i)
    while test_list[0] < K:
        if len(test_list) <= 1:
            return -1
        f = heapq.heappop(test_list)
        s = heapq.heappop(test_list)
        summ = f+(2*s)
        heapq.heappush(test_list, summ)
        answer += 1
        
    return answer