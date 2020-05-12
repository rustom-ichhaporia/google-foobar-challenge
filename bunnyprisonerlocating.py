# Rustom Ichhaporia

def solution(x, y):
    yAdjusted = y - 1
    origin = x + yAdjusted
    id = origin * (origin + 1) // 2
    id -= yAdjusted
    return str(id)

print(solution(1,5))