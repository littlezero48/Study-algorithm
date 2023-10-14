def solution(arr1, arr2):
    # 행렬의 곱셈 개념을 알아야 함
    # 앞배열의 한 행을 뒷배열의 열에 곱함
    # [[A11,A12],[A21,A22],[A31,A32]] 행3 * [[B11,B12],[B21,B22]] 열2
    # = [[(A11*B11)+(A12*B21), (A11*B12)+(A12*B22)],
    #    [(A21*B11)+(A22*B21), (A21*B12)+(A22*B22)],
    #    [(A31*B11)+(A32*B21), (A31*B12)+(A32*B22)]] 
    answer = []
    
    for i in range(len(arr1)): # arr1 행
        answer1 = []
        for j in range(len(arr2[0])): # arr2 열
            num = 0     
            
            for k in range(len(arr1[0])): # arr1 열
                num += arr1[i][k] * arr2[k][j]                  
            answer1.append(num)  
            
        answer.append(answer1)
    
    return answer