# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    def convert(n, base):
        T = "0123456789ABCDEF"
        
        q, r = divmod(n, base)
        
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    
    check = '0'
    i = 1
    
    while len(check) < t * m:
        check += convert(i, n)
        
        i += 1
        
    result = ''
        
    for i in range(p - 1, t * m, m):
        result += check[i]
        
    return result