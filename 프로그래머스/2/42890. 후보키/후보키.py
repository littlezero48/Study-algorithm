from itertools import combinations

def solution(relation):
    # relation은 2차원 배열
    row = len(relation) # 행
    col = len(relation[0]) # 열

    # 모든 relation 테이블에서 생성할 수 있는 인덱스 조합을 만든다
    combi = []
    for i in range(1, col+1): # i: 조합이 될 열의 갯수
        combi.extend(combinations(range(col), i))
   
    # 후보키가 될 인덱스 조합을 모을 배열
    unique = []    
    # 모든 인덱스 조합을 모두 조회 
    for i in combi:
        # 인덱스를 모두 값으로 치환
        tmp = [tuple([item[key] for key in i]) for item in relation]

        # set 자료형은 고유한 속성만을 모을수 있기 때문에 set 길이와 기존 row 길이가 같다면 유일성을 만족
        if len(set(tmp)) == row: 
            put = True
            
            # 후보키 조합이
            for x in unique:
                # isdisjoint : 전혀 공통요소가 없는 집합인가?
                # issubset : A가 B에 포함되어 있을때 A(부분 집합)인가? 
                # issuperset : A가 B에 포함되어 있을때 B(확대 집합)인가?
                if set(x).issubset(set(i)):  # set(x)가 set(i)의 부분 집합이라면 최소성 만족할 수 없으므로
                    put = False # 후보키에서 탈락
                    break

            if put : # 후보키 조건에 만족한 것만 unique 배열에 넣는다
                unique.append(i) 

    return len(unique)