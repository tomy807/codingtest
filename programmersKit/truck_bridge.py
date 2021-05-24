from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge=deque([0]*bridge_length)
    truck_weights=deque(truck_weights)
    answer=0
    bridge_weight=0
    while bridge:
        right=bridge.popleft()
        bridge_weight-=right
        answer+=1
        if truck_weights:
            if bridge_weight+truck_weights[0]>weight:
                bridge.append(0)
            else:
                left=truck_weights.popleft()
                bridge.append(left)
                bridge_weight+=left
    return answer
print(solution(2,10,[7,4,5,6]))