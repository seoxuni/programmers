#120864
import re
def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)
    for number in list(map(int, numbers)):
        answer += number
    
    return answer
    #return sum([int(i) for i in re.findall(r'\d+', my_string)])