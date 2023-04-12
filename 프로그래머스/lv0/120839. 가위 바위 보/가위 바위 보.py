def solution(rsp):
    rsp_arr = [('2','0'),('0','5'),('5','2')]
    answer = ''
    for i in range(0,len(rsp)) :
        for one_rsp_arr in rsp_arr :
            if one_rsp_arr[0] == rsp[i] :
                answer += one_rsp_arr[1]
    return answer