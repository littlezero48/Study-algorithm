def solution(s):
    answer = [0, 0]
    
    # 이진법 처리 
    def makeBinary(str_num):
        if str_num == "1" :
            return
        
        original_len =  len(str_num)
        replace_len = len(str_num.replace("0",""))
        diff_oNr = original_len - replace_len
        
        bin_arr = []
        while replace_len > 1 : 
            quotient, remainder = divmod(replace_len, 2)
            bin_arr.append(remainder)
            replace_len = quotient
            
        bin_arr.append(replace_len)
        bin_arr.sort(reverse=True)
        len_binary = "".join([str(_) for _ in bin_arr])
        answer[1] += diff_oNr
        answer[0] += 1
        
        if len_binary != 1 :
            makeBinary(len_binary)
        
    makeBinary(s)  
    return answer
    