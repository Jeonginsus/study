def solution(n):
    answer = ''
    if n == 3:
        return "4"
    while n:
        if n%3 == 0:
            n -= 3
        left = n%3
        if left:
            answer += str(left)
        else:
            answer += "4"
        n = n//3
    return answer[::-1]