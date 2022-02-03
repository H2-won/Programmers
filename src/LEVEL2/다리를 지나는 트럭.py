def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0 for _ in range(bridge_length)]
    sumOnBridge = 0
    while onBridge:
        answer += 1
        poped = onBridge.pop(0)
        if  poped != 0:
            sumOnBridge -= poped
        
        if truck_weights:
            if sumOnBridge + truck_weights[0] <= weight:
                poped = truck_weights.pop(0)
                onBridge.append(poped)
                sumOnBridge += poped
            else:
                onBridge.append(0)
            
    return answer
  
# sum(onBridge) 를 사용하면 if truck_weights: 문 한번 들어갈떄마다 sum을 실행해서 시간이 매우 느려짐
# -> sum 함수가 아닌 sumOnBridge변수를 활용해서 시간 단축