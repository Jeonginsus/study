def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    test_list = [s//n]*n
    for a in range(s%n):
        test_list[a] += 1
    answer = sorted(test_list)
    return answer