def solution(n, m, x, y, queries):
    answer = 0
    answer_square = [x, x, y, y]
    reverse_query = list(reversed(queries))
    for rq in reverse_query:
        _d, _v = rq
        if _d == 0:
            if answer_square[2] == 0:
                answer_square[3] += _v
            else:
                answer_square[3] += _v
                answer_square[2] += _v
        elif _d == 1:
            if answer_square[3] == m-1:
                answer_square[2] -= _v
            else:
                answer_square[3] -= _v
                answer_square[2] -= _v
        elif _d == 2:
            if answer_square[0] == 0:
                answer_square[1] += _v
            else:
                answer_square[1] += _v
                answer_square[0] += _v
        elif _d == 3:
            if answer_square[1] == n-1:
                answer_square[0] -= _v
            else:
                answer_square[0] -= _v
                answer_square[1] -= _v
        answer_square[0] = max(answer_square[0], 0)
        answer_square[1] = min(answer_square[1], n-1)
        answer_square[2] = max(answer_square[2], 0)
        answer_square[3] = min(answer_square[3], m-1)
        if answer_square[0] > n-1 or answer_square[1] < 0 or answer_square[2] > m-1 or answer_square[3] < 0:
            answer = 0
            break
    else:
        answer = (answer_square[1]-answer_square[0]+1)*(answer_square[3]-answer_square[2]+1)
    return answer