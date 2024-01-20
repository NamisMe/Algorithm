def solution(participant, completion):
    participant_dict = {}
    completion_dict = {}
    
    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    
    for c in completion:
        if c in completion_dict:
            completion_dict[c] += 1
        else:
            completion_dict[c] = 1
    
    print(participant.items())

    for p, count in participant_dict.items():
        if p not in completion_dict or count > completion_dict[p]:
            return p
        
    
            