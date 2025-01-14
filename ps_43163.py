# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    count = 1
    check_words = [begin]
    checked_words = set()
    words_set = set()
    
    words_set.add(begin)
    
    while True:
        next_check = []
        
        for i in check_words:
            for j in range(len(begin)):
                check_word = i[: j] + i[j + 1: ]
                
                if (check_word, j) in checked_words:
                    continue
                else:
                    checked_words.add((check_word, j))
                
                for v in words:
                    if check_word == v[: j] + v[j + 1: ] and v not in words_set:
                        if v == target:
                            return count
                        else:
                            next_check.append(v)
                            words_set.add(v)
        
        if next_check == []:
            return 0
            
        count += 1
        check_words = next_check