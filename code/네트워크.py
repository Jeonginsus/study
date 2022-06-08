def solution(n, computers):
    answer = 0
    test_list = [0]*n
    for a in range(n):
        if not test_list[a]:
            answer += 1
            test_list[a] = answer
            deq=[]
            deq.append(computers[a])
            while deq:
                d = deq.pop(0)
                for inner_d in range(n):
                    if not test_list[inner_d] and d[inner_d] == 1:
                        test_list[inner_d] = answer
                        deq.append(computers[inner_d])          
    return answer