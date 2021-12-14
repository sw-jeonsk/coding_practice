from collections import Counter
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]


def my_solution(_lottos, _win_nums):

    total_count = Counter(_lottos + _win_nums)
    same_count, zero_count = 0, 0

    for key, value in total_count.most_common():
        # 당첨 갯수
        if key != 0 and value == 2:
            same_count += 1
        elif key == 0:
            zero_count = value
    lowest = 7 - same_count if same_count > 1 else 6
    best = 7 - (same_count + zero_count) if (same_count + zero_count) > 1 else 6
    answer = [best, lowest]
    return answer

def best_solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


print(solution(lottos, win_nums))