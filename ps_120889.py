def solution(sides):
    sides = sorted(sides)
    
    return abs(int(sides[0] + sides[1] > sides[2]) - 2)