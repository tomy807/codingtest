def solution(s):
    return ' '.join(map(lambda s: s[0].upper() + s[1:].lower() if s else s, s.split(' ')))
print(solution('aaaaa    aaa'))