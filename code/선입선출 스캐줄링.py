def is_over(n, cores, num):
    return_list = []
    re = 0
    for c in range(len(cores)):
        co = cores[c]
        if num % co == 0:
            return_list.append(c+1)
        re += (num // co)+1
    if re >= n:
        return (return_list, re-n)
    return (False, False)
        
def solution(n, cores):
    if n <= len(cores):
        return n
    left = 0 
    right = sum(cores)//(len(cores)-1)*n
    mid = -1
    while True:
        if mid == (left+right)//2:
            break
        mid = (left+right)//2
        ll, ln = is_over(n, cores, mid)
        
        if ll != False:
            answer_list, idx = ll, ln
            right = mid
        else:
            left = mid

    return answer_list[-idx-1]