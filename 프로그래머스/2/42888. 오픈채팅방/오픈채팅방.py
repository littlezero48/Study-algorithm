def solution(record):
    answer = []
    uid_list = {} # dict = uid : nickname
    
    # 결국 가장 마지막에 기록된 유저 닉네임을 기준으로 출력하는 방식
    # 닉네임 정보 먼저 정리
    
    for one in record:
        one_list = one.split()      
        # 나간거 빼고 닉네임 체크
        if one_list[0] == 'Leave':
            continue
        uid_list[one_list[1]] = one_list[2]

    # 정리된 닉네임을 기준으로 출력
    for chat_one in record:
        chat_list = chat_one.split()
        if chat_list[0] == "Enter":
            answer.append(uid_list[chat_list[1]]+"님이 들어왔습니다.")
        elif chat_list[0] == "Leave":
            answer.append(uid_list[chat_list[1]]+"님이 나갔습니다.")
    
    return answer