#181880
def solution(num_list):
    count = 0
    tmp = 0
    for i in num_list:
        tmp = i
        while tmp != 1:
            if tmp % 2 == 0:
                tmp //= 2
                count += 1
            else:
                tmp = (tmp - 1) // 2
                count += 1
                
    return count

#def solution(num_list):
#    answer = 0
#    
#    for i in num_list:
#        while i != 1:
#            i //= 2
#            answer += 1
#                
#    return answer