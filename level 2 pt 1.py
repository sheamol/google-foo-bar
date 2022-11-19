def solution(l):
    answer = [[int(j) for j in i.split('.')] for i in l]

    answer.sort()
    answer = ['.'.join([str(k) for k in i]) for i in answer]

    return answer


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
