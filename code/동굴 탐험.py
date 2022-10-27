def solution(n, path, order):
    links = [[] for _ in range(n)]
    banneds = {}
    vis = [0]*n
    
    for s, e in path:
        links[s].append(e)
        links[e].append(s)
        
    for p, b, in order:
        banneds[p] = b
        vis[b] = p
        
    que = [0]
    
    if vis[0] == 0:
        vis[0] = -1
        bl = banneds.get(0)
        if bl:
            vis[bl] = 0
        
        while que:
            c = que.pop(0)
            for l in links[c]:
                if vis[l] == 0:
                    que.append(l)
                    vis[l] = -1
                    bl = banneds.get(l)
                    if bl:
                        if vis[bl] == -2:
                            que.append(bl)
                            vis[bl] = -1
                        else:
                            vis[bl] = 0
                elif vis[l] > 0:
                    vis[l] = -2
                    
    return n == vis.count(-1)