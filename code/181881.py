#조건에 맞게 수열 변환하기 2 (181881)
def solution(arr):
    answer = 0
    while True:
        tmp = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                tmp.append(i//2)
            elif i < 50 and i % 2 == 1:
                tmp.append(i*2+1)
            else:
                tmp.append(i)
        
        if arr == tmp:
            return answer
        else:
            answer += 1
            arr = tmp