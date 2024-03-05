import string

def solution(N):
    alphabet = string.ascii_lowercase
    generated_string = []
    common_occurrence = 1
    letter_index = 0
    while N // common_occurrence > 26:
        common_occurrence += 1
    while len(generated_string) < N:
        generated_string.extend(alphabet[letter_index] * common_occurrence) # add equal number of characters
        letter_index += 1
    generated_string = generated_string[0:N] # cutoff the extra characters
    return ''.join(generated_string)

# usage
print(solution(70))