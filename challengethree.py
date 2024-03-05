import string

alphabet = string.ascii_lowercase
print(alphabet)

def solution(N):
    generated_string = []
    common_occurrence = N//26
    last_letters = N % 26
    for i in range(27):
        generated_string.extend(alphabet[i] * common_occurrence)
    print(''.join(generated_string))

solution(53)