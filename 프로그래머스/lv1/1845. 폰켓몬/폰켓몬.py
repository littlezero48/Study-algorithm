def solution(nums):
    answer = 0
    all_nums = len(set(nums))
    choice = len(nums) //2
    if(all_nums > choice):
        answer = choice
    else :
        answer = all_nums
    return answer