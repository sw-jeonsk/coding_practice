# https://programmers.co.kr/learn/courses/30/lessons/60057
import pdb
# aabbcc


def solution(s):
    answer = 0

    for length in range(1, len(s)):
        split_s(s, length)
    text, index = dup_counting_slice(3, s)
    print ( text, index)
    return answer

def split_s(s, length):
    for length in range(1, len(s)):
        split_s(s, length)


def dup_counting_slice(length, s):
    cmp_s, count = "", 1

    for index in range(0, len(s), length):
        print(cmp_s, s[index:index + length])
        if cmp_s == "":
            cmp_s = s[index:index + length]
        elif cmp_s == s[index:index + length]:
            count += 1
        else:
            return count, cmp_s

solution('dededededede')