from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    difference = participant_counter - completion_counter
    
    return list(difference.keys())[0]