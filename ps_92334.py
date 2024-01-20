# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    result = [0] * len(id_list)
    report_list = [0] * len(id_list)

    report = set(report)
    
    for i in report:
        report_id = i.split()
        
        report_list[id_list.index(report_id[1])] += 1
        
    for i, v in enumerate(report_list):
        if v >= k:
            for j, w in enumerate(id_list):
                report_str = w + " " + id_list[i]
                
                if report_str in report:
                    result[j] += 1
    
    return result