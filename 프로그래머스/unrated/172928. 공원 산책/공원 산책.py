def solution(park, routes):
    now = [0,0]
    
    # 시작점 
    for i in range(0,len(park)):
        if 'S' in park[i]:
            now[0] = i                      # 행
            now[1] = park[i].index('S')     # 열
            
    x1 = y1 = 0
    # Route 판별
    for route in routes :
        
        # 공원 밖인지 판별
        if route[0] == 'E' :
            x1 = now[1] + int(route[2])
            if x1 > len(park[0])-1 :
                continue
        elif route[0] == 'W' :
            x1 = now[1] - int(route[2])
            if x1 < 0 :
                continue
        elif route[0] == 'S' :
            y1 = now[0] + int(route[2])
            if y1 > len(park)-1 :
                continue
        elif route[0] == 'N' :
            y1 = now[0] - int(route[2])
            if y1 < 0 :
                continue

        b_x = b_y = a_x = a_y = 0    
        # 장애물 판별
        if route[0] == 'E' or route[0] == 'W' : 
            if now[1] > x1 :
                b_x = x1
                a_x = now[1]
            else :
                b_x = now[1]+1
                a_x = x1+1
                
            if 'X' in park[now[0]][b_x:a_x]:
                continue
            else :
                now[1] = x1
        else :  
            if now[0] > y1 :
                b_y = y1
                a_y = now[0]
            else :
                b_y = now[0]+1
                a_y = y1+1

            if 'X' in [ park[j][now[1]] for j in range(b_y,a_y) ]:
                continue
            else :
                now[0] = y1
                
    return now