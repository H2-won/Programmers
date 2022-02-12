from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
        cache.append(i)
    return answer

# cache = deque(maxlen=cacheSize)를 사용하면 append 할때 알아서 앞에꺼 밀려서 삭제됌
# deque를 사용하면 popleft가 O(1)이다. 사용 안하면 popleft 작업이 O(n)임 땡겨야 되니까