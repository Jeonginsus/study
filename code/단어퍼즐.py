def solution(strs, t):
    lt = len(t)
    test_list = [20001] * lt +[0]
    memo = {}
    t_w = ""
    for s in strs:
        memo[s] = True
    for le in range(len(t)-1, -1, -1):
        for ri in range(1, 6):
            if le+ri <= lt:
                if memo.get(t[le:le+ri]):
                    test_list[le] = min(test_list[le], test_list[le+ri]+1)
#     for a in range(5):
#         t_w += t[a]
#         if memo.get(t_w) == True:
#             test_list[a] = 1
#     t_w = ""
#     for a in range(len(t)):
#         t_w += t[a]
        
#         if len(t_w) > 5:
#             t_w = t_w[1:]
            
#         for wl in range(5):
#             lew = len(t_w)
#             if lew>wl :
#                 if a-lew+wl >= 0 and memo.get(t_w[wl:]) == True:
#                     test_list[a] = min(test_list[a], test_list[a-lew+wl]+1)
#     print(test_list)
    if test_list[0] == 20001:
        return -1
    return test_list[0]