def solution(myStr):
    answer = list(filter(None, myStr.replace('a', '_').replace('b', '_').replace('c', '_').split('_')))
    return answer if answer else ["EMPTY"]