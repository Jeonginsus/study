def remove_rock(rocks, min_distance, n, distance):
    s_p = 0
    _count = 0
    for r in rocks:
        if (r-s_p)<min_distance:
            _count += 1
        else:
            s_p = r
        if _count > n:
            return True
    else:
        if (distance-s_p)<min_distance:
            _count += 1
        if _count > n:
            return True
    return False
def solution(distance, rocks, n):
    rocks.sort()
    left = 0
    right = distance
    answer  = 0
    while True:
        if answer == (left+right)//2:
            break
        answer = (left+right)//2
        if remove_rock(rocks, answer, n, distance):
            right = answer
        else:
            left = answer
    
    return answer