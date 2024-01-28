def solution(files):
    answer = []
    
    file_multi_array = []
    
    # 숫자가 나오면 NUMBER시작
    for file in files :
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit(): # 숫자가 나오면 number 시작
                head = file[:i]
                number = file[i:]
                
                #숫자가 더이상 안나오면 tail 시작
                for j in range(len(number)):
                    if not number[j].isdigit():                        
                        tail = number[j:]  
                        # number에 먼저 number 자른 부분만 넣어주게 되면 tail은 다 사라지므로 먼저 tail 넣어주고 number 자르기
                        number = number[:j] 
                        break
                
                file_multi_array.append([head, number, tail])
                break
              
    # 파이썬 다차원 배열 정렬 방식 참조
    # sort(key=lambda x:(x[0], x[1]))
    # 그리고 sort 방식이 stable방식의 정렬인 것도 기억할 것 (같은 값일 경우 입력순으로 정렬)
    # 정렬 1조건 대소문자구분X 하나로 통일해 정렬
    # 정렬 2조건 앞에 0이 붙더라도 0무시 숫자로 정렬
    # tail은 정렬에 영향 없음
    file_multi_array.sort(key=lambda x:(x[0].lower(), int(x[1])))                
    
    return [''.join(fileOne) for fileOne in file_multi_array]