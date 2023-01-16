def solution(progresses, speeds):
    release_cnt = 0
    day = 0
    answer = []
    
    while len(progresses) > 0 :
        if (progresses[0] + speeds[0] * day) >= 100 :
            release_cnt = release_cnt + 1
            progresses.pop(0)
            speeds.pop(0)
        else :
            if release_cnt > 0 :
                answer.append(release_cnt)
                release_cnt = 0
            day = day + 1
    answer.append(release_cnt) 
            
    return answer


    
    
    