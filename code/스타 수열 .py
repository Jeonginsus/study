def solution(a):
    answer = 0
    test_list = {}
    for nn in a:
        if nn in test_list:
            test_list[nn] += 1
        else:
            test_list[nn] = 1
    if len(a) < 4:
        answer = 0
    else:
        for n in test_list.keys():
            if test_list[n]*2 <= answer:
                continue
            n1 = False
            n2 = False
            ans = 0
            for na in a:
                if na == n:
                    if n1:
                        n1 = False
                        n2 = False
                        ans += 2
                    else:
                        n2 = True
                else:
                    if n2:
                        n1 = False
                        n2 = False
                        ans += 2
                    else:
                        n1 = True
                answer = max(ans, answer)
    if answer < 4:
        answer = 0
    return answer