def solution(s):
    answer = ""
    s_arr = [int(one) for one in s.split(" ")]
    answer += str(min(s_arr)) + " " + str(max(s_arr))
    return answer