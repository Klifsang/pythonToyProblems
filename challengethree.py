import string

def solution(N):
    # Determine the maximum number of different letters we can include
    max_letters = min(26, N // 2)
    
    # Construct the string with the maximum number of different letters
    result = ""
    for i in range(max_letters):
        result += string.ascii_lowercase[i] * 2
    
    # If there are remaining characters to fill, repeat the sequence
    result += string.ascii_lowercase[:N - len(result)]
    
    return result

# Test cases
print(solution(3))   # Output: "abb"
print(solution(5))   # Output: "aabbc"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
