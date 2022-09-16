def solution(money):
    answer = 0
    money1 = money[:-1]
    money2 = money[1:]
    test_list1 = [0]*2 + [0]*(len(money)-1)
    test_list2 = [0]*2 + [0]*(len(money)-1)
    for m in range(len(money1)):
        test_list1[m+2] = max(test_list1[m+1], test_list1[m] + money1[m])
        test_list2[m+2] = max(test_list2[m+1], test_list2[m] + money2[m])
    answer = max(test_list1[-1], test_list2[-1])
    return answer