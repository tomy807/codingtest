from string import ascii_lowercase,ascii_uppercase
def solution(s, n):
    low_alphabet_list = list(ascii_lowercase)
    up_alphabet_list = list(ascii_uppercase)
    answer = ''
    for char in s:
        if char==' ':
            answer+=' '
        else:
            if char in low_alphabet_list:
                answer+=low_alphabet_list[(low_alphabet_list.index(char)+n)%26]
            else :
                answer+=up_alphabet_list[(up_alphabet_list.index(char)+n)%26]
    return answer
print(solution("AB", 1))