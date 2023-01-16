def solution(nums):
    all_nums = len(set(nums))
    choice = len(nums) // 2
    answer = choice if all_nums > choice else all_nums 
    return answer