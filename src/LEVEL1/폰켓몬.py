def solution(nums):
    get = len(nums)/2
    kinds = len(set(nums))
    
    return min(get, kinds)