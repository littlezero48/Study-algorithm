def solution(t, p):
    
    cnt = 0
    # len 길이 구하는 식
    unit = len(p)
    # 한줄 포문 앞에 실행문 두고 뒤에 for문을 둔다.
    # 리스트 표현식에는 리스트 안에 if문과 for을 넣을 수 있음
    b = [t[i:i+unit] for i in range(0,len(t))]
    print(b)

    for one in b:
        if int(one) <= int(p) and len(one) == len(p):
            cnt += 1

    return cnt