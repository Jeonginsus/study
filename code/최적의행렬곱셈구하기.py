def solution(matrix_sizes):
    answer = 0
    lms =len(matrix_sizes)
    test_list =list([999999999]*lms for _ in range(lms))
    for a in range(lms):
        test_list[a][a] = 0
    for _len in range(1, lms):
        for start in range(lms):
            end = start + _len
            if end >= lms:
                break
            for _middle in range(start, end):
                test_list[start][end] = min(test_list[start][end], test_list[start][_middle]+test_list[_middle+1][end]+(matrix_sizes[start][0]*matrix_sizes[end][1]*matrix_sizes[_middle][1]))
    answer = test_list[0][lms-1]
    return answer