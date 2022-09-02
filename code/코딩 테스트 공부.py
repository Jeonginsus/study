def solution(alp, cop, problems):
    answer = 0
    max_alp = 0
    max_cop = 0
    
    for a in range(len(problems)):
        max_alp=max(max_alp, problems[a][0])
        max_cop=max(max_cop, problems[a][1])
        
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    DP=list(list([150]*(max_cop+1)) for _ in range(max_alp+1))
    DP[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            
            if i+1 <= max_alp:
                DP[i+1][j] = min(DP[i+1][j], DP[i][j]+1)
                
            if j+1 <= max_cop:
                DP[i][j+1] = min(DP[i][j+1], DP[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(max_alp, i+alp_rwd), min(max_cop, j+cop_rwd)
                    DP[next_alp][next_cop] = min(DP[next_alp][next_cop], DP[i][j]+cost)
    answer = DP[-1][-1]
    return answer