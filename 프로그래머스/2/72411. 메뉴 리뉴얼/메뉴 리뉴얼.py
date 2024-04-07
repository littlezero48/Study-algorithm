from itertools import combinations  # 조합
from collections import Counter       

def solution(orders, course):
    answer = []
    # 코스 크기에 따른 For문
    for course_size in course:
        order_comb = []        
        for order in orders:
            # 주문한 내용을 먼저 정렬, 그리고 코스 크기에 따른 모든 조합 생성
            order_comb += combinations(sorted(order), course_size)
            
        # Count() : 카운팅하여 많은 순으로 dict 형태로 리턴
        # moste_common() : 많은 순으로 정렬된 튜플 배열 리턴
        most_ordered = Counter(order_comb).most_common()        
        
        if len(most_ordered) == 0: # 정리된 배열이 없다면 통과
            continue

        # 가장 카운팅 많은 코스의 수를 가져옴
        max_value = most_ordered[0][1]
        
        for key, value in most_ordered:
            # 카운팅된 것 중 최소 2개 이상 이면서 가장 많이 주문된 코스를 answer에 추가 
            if value > 1 and value == max_value:
                answer.append(''.join(key)) # answer 추가시 배열을 문자열로 수정

    return sorted(answer) # 오름차순 배열