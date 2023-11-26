def solution(phone_book):
    answer = True
    
    # A가 B의 접두어라면 정렬시 A가 일단 길이가 같거나 짧아야하고 앞서 있어야하며 서로 "인접"하게 된다
    phone_book.sort() 
    
    for i in range(len(phone_book)-1):
        # 접두어 판별, 앞번호 == 뒷번호의 앞번호 만큼 길이를 잘라 동일한지 비교
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            # 동일하다면 접두어가 존재하므로 바로 break로 빠져나와 return
            answer = False
            break
    
    return answer