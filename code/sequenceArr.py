#120835
def solution(emergency):
    x = sorted(emergency, reverse=True)
    return [x.index(i) + 1 for i in emergency]