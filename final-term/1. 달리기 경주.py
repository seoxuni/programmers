def solution(players, callings):
    result = {}
    for i, p in enumerate(players):
        result[p] = i
        
    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players