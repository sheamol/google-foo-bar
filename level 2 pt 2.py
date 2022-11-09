def solution(h, q):
    
    return [step_back(h, target) for target in q]

def step_back(height, target):

    current = (2 ** height) - 1 
    previous = -1
    next = current

    while next > 0:
        
        if current == target:
            return previous
        
        previous = current
        next = next >> 1

        left = current - next - 1
        right = current - 1
        
        if target <= left:
            current = left
        elif target >= left:
            current = right

    return -1           


print(solution(3, [7, 3, 5, 1]))

print(solution(5, [19, 14, 28]))