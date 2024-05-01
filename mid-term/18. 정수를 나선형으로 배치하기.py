#정수를 나선형으로 배치하기
def solution(n):
    answer = []
    if n == 1:
        return [[1]]

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        answer.append(row)
        
    x = 0
    y = 0
    dir = 'r'
    
    for i in range(n*n):
        answer[x][y] = i + 1
        if dir == 'r':
            y += 1
            if y == n - 1 or answer[x][y+1] != 0:
                dir = 'd'
        elif dir == 'd':
            x += 1
            if x == n - 1 or answer[x+1][y] != 0:
                dir = 'l'
        elif dir == 'l':
            y -= 1
            if y == 0 or answer[x][y-1] != 0:
                dir = 'u'
        elif dir == 'u':
            x -= 1
            if x == n -1 or answer[x-1][y] != 0:
                dir = 'r'
    
    return answer