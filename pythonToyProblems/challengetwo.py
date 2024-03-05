def digit_sum(n):
    return sum(map(int, str(n)))

def solution(A):
    max_sum = -1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if digit_sum(A[i]) == digit_sum(A[j]):
                max_sum = max(max_sum, A[i] + A[j])
    return max_sum

# usage
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))      # Output: 102
print(solution([51, 32, 43]))      # Output: -1
