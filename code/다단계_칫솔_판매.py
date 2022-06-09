def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    per_dic ={}
    for e in range(len(enroll)):
        per_dic[enroll[e]] = e
    for n in range(len(seller)):
        p_name = seller[n]
        p_cost = amount[n]*100
        while True:
            if referral[per_dic[p_name]] == "-":
                answer[per_dic[p_name]] += p_cost-(p_cost//10)
                break
            else:
                answer[per_dic[p_name]] += p_cost-(p_cost//10)
                p_cost = p_cost//10
                if p_cost == 0:
                    break
                p_name = referral[per_dic[p_name]]
    return answer