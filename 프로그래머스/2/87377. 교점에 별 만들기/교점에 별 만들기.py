def solution(line):
    answer = []
    points = set() # 동일한 점은 한개로
      
    # 교점 구하기
    line_cnt = len(line)
    for i in range(line_cnt):
        for j in range(i+1, line_cnt):           
            a, b, e = line[i]
            c, d, f = line[j]
            
            # 교점 구하는 방식은 참고사항에 설명
            # x = (BF-ED)/(AD-BC)
            # y = (EC-AF)/(AD-BC)            
            if a*d - b*c != 0 :  # AD-BC = 0 은 두직선이 평행 또는 일치
                x = (b*f - e*d)/(a*d - b*c)
                y = (e*c - a*f)/(a*d - b*c)
                
            if int(x) == x and int(y) == y : # 직선의 교점 중 정수 좌표!
                points.add((int(x), int(y)))
    
    # x의 최소, 최대, y의 최소, 최대로 격자판 최대 좌표 설정 
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # 좌표를 왼쪽 위에서부터 그려야하므로 max_y와 min_x가 가장 첫번째 시작이어야 함
    for y in range(max_y, min_y-1, -1): # y값은 점점 줄어야 
        y_row = ""
        for x in range(min_x, max_x+1, 1): # x값은 점점 늘어야        
            if (x, y) in points :
                y_row += "*"
            else : 
                y_row += "."
        answer.append(y_row)
    
    return answer