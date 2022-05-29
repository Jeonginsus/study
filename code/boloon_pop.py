def solution(a):
    answer = 0
    test_list = [False]*len(a)
    left_num = 1000000001
    right_num = 1000000001
    for left_n in range(len(a)):
        if left_num > a[left_n]:
            left_num = a[left_n]
            if test_list[left_n] == False:
                answer += 1
                test_list[left_n] = True
                
    for right_n in range(len(a)-1, -1, -1):
        if right_num > a[right_n]:
            right_num = a[right_n]
            if test_list[right_n] == False:
                answer += 1
                test_list[right_n] = True
    return answer