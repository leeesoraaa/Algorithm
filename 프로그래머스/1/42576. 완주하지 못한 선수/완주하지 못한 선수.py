# def solution(participant, completion):
#     answer = ''
#     for p in participant:
#         if participant.count(p) > completion.count(p):
#             answer = p                   
#     return answer

# def solution(participant, completion):

#     p = sorted(participant)
#     c = sorted(completion)

#     for i, j in zip(p, c):

#         if i != j:
#             return i
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]