# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    result = ""
    
    left_hand = [0, 0]
    right_hand = [2, 0]
    
    left_set = {1, 4, 7}
    right_set = {3, 6 ,9}
    
    numbers_dict = {0: [1, 0], 1: [0, 3], 2: [1, 3], 3: [2, 3], 4: [0, 2], 5: [1, 2], 6: [2, 2], 7: [0, 1], 8: [1, 1], 9: [2, 1]}
    
    for i in numbers:
        if i in left_set:
            result += "L"
            
            left_hand = numbers_dict[i]
        elif i in right_set:
            result += "R"
            
            right_hand = numbers_dict[i]
        else:
            if abs(left_hand[0] - numbers_dict[i][0]) + abs(left_hand[1] - numbers_dict[i][1]) < abs(right_hand[0] - numbers_dict[i][0]) + abs(right_hand[1] - numbers_dict[i][1]):
                result += "L"
            
                left_hand = numbers_dict[i]
            elif abs(left_hand[0] - numbers_dict[i][0]) + abs(left_hand[1] - numbers_dict[i][1]) > abs(right_hand[0] - numbers_dict[i][0]) + abs(right_hand[1] - numbers_dict[i][1]):
                result += "R"
            
                right_hand = numbers_dict[i]
            else:
                if hand == "left":
                    result += "L"
            
                    left_hand = numbers_dict[i]
                else:
                    result += "R"
            
                    right_hand = numbers_dict[i]
                
    return result