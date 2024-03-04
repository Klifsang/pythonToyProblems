target = 10

def solution(A):
    count = 0
    for index, number in enumerate(A):
        if number != target and index + 1 < len(A):
            required = target - number
            count += abs(required)
            A[index] = target
            A[index+1] = A[index+1] - required

    if A[len(A)-1] != target:
        return -1
    else:
        return count



# usage
print(solution([7, 15, 10, 8]))  # print 7
print(solution([11, 10, 8, 12, 8, 10, 11])) # print 6
print(solution([7, 14, 10])) # print -1