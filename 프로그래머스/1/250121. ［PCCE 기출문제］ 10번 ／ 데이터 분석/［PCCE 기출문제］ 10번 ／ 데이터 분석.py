def solution(data, ext, val_ext, sort_by):
    answer = []
    # 기준 정보에 대한 인덱스 값을 dictionary로 정리
    dict = {"code":0, "date":1, "maximum":2, "remain":3}
    for d in data:
        # 기준 정보의 인덱스 값 할당
        value = d[dict[ext]]
        # 정보 기준값 이하
        if value <= val_ext:
            answer.append(d)
    # 정렬 조건을 대상으로 오름차순
    answer.sort(key = lambda x : x[dict[sort_by]])
    return answer