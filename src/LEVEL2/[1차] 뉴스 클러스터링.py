from collections import Counter

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            list1.append(str1[i] + str1[i+1])
            
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            list2.append(str2[j] + str2[j+1])
            
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    intersection = list((c1 & c2).elements())
    union = list((c1 | c2).elements())
    
    if len(union) == 0 and len(intersection) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)