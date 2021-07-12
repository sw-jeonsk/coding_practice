import collections

def my_solution(participant, completion):
    completion.sort()
    participant.sort()
    for a, b in zip(participant, completion):
        if a != b:
            return a

    return participant[len(participant)-1]




def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]