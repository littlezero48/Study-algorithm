from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    # 원하는 항목과 갯수를 하나로 zip
    for w, n in zip(want, number):
        check[w] = n
    
    print(check)
    
    for i in range(len(discount)-9): # 마지막 9일 동안은 10일간의 회원 기간으로 부족하므로 기준 날짜에서 제외
        c = Counter(discount[i:i+10]) # 매일을 기준으로 원소 개수를 확인
        if c == check: # 위에 정리한 정보와 일치하면 모두 할인 받을수 있는 일수 +1
            answer += 1

    return answer