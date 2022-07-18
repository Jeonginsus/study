def test(stones, k, _num):
    _sum_num = 0
    for a in range(len(stones)):
        if stones[a] <= _num:
            _sum_num += 1
        else:
            _sum_num = 0
        if _sum_num == k:
            return True
    return False

def solution(stones, k):
    answer = 0
    _max = 200000000
    _min = 1
    _middle = 0
    while True:
        if _middle == (_max+_min)//2:
            if not test(stones, k, _middle):
                _middle+=1
            break
        _middle = (_max+_min) // 2
        if test(stones, k, _middle):
            _max = _middle
        else:
            _min = _middle
    answer = _middle
    return answer