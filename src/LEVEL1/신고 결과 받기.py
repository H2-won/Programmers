def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reportedDict = {id:[] for id in id_list}
    report = list(set(report))
    for i in report:
        reporting, reported = i.split()
        reportedDict[reported].append(reporting)

    for key, value in reportedDict.items():
        if len(value) >= k:
            for i in value:
                answer[id_list.index(i)] += 1
        
    return answer