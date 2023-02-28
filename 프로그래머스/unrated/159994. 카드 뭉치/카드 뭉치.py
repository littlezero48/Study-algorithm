def solution(cards1, cards2, goal):
    for one in goal:
        if len(cards1) != 0 and cards1[0] == one :
            cards1.pop(0)
        elif len(cards2) != 0 and cards2[0] == one :
            cards2.pop(0)
        else :
            return "No"

    return "Yes"