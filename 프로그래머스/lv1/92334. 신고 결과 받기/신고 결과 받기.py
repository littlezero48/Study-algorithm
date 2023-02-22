def solution(id_list, report, k):

    declare_dict = {}
    for one in report:
        declare_from, declare_to = one.split(" ")                   # 신고자와 신고대상을 나눔

        if declare_to in declare_dict :                             # 신고 내역 확인
            if declare_from not in declare_dict[declare_to] :       # 동일한 신고자는 제외
                declare_dict.get(declare_to).append(declare_from)   # 신고자 배열 가져와서 추가
        else :
            declare_dict[declare_to] = [declare_from]

    mail_receivers = []
    for key, value in declare_dict.items() :
        if len(value) >= k :
            mail_receivers.extend(value)

    result = []
    for id in id_list :
        result.append(mail_receivers.count(id))

    return result