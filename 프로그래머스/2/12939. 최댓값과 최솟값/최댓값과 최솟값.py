def solution(s):
    answer = ""
    s_arr = s.split(" ")
    answer += min(s_arr) + " " + max(s_arr)
    return answer