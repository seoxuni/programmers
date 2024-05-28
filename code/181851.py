#181851
def solution(rank, attendance):
    t = []
    for i in range(len(rank)):
        if attendance[i]:
            t.append(rank[i])
        
    t.sort()
    
    return 10000 * rank.index(t[0]) + 100 * rank.index(t[1]) + rank.index(t[2])