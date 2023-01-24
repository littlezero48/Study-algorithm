def solution(triangle):
    
    new_Triangle = []
    for idx in range(0, len(triangle)) :
        list = []
        for idx2 in range(0, len(triangle[idx])) :
            list.append(0)
        new_Triangle.append(list)

    for idx in range(0, len(triangle)-1) :
        if idx == 0 :
            # 시작값은 바로 넣어주기
            new_Triangle[0] = triangle[0]

        for idx2, value2 in enumerate(triangle[idx]):
            #중간숫자
            first_Int = new_Triangle[idx][idx2]

            #왼쪽
            plus_Int1 = triangle[idx+1][idx2]
            sum1 = first_Int + plus_Int1
            if new_Triangle[idx+1][idx2] < sum1 :
                new_Triangle[idx+1][idx2] = sum1

            #오른쪽
            plus_Int2 = triangle[idx+1][idx2+1]
            sum2 = first_Int + plus_Int2
            if new_Triangle[idx+1][idx2+1] < sum2 :
                new_Triangle[idx + 1][idx2 + 1] = sum2
                
    # 마지막 결과중에서 가장 큰 값 리턴
    return max(new_Triangle[len(new_Triangle)-1])