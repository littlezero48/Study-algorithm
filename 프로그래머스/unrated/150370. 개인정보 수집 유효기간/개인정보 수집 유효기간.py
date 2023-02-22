def solution(today, terms, privacies):
    result = []
    t_year, t_month, t_day = today.split('.')

    # 현재 시간과 수집 시간의 날짜 차이와 만료 기간 날짜 간의 차이를 비교
    for i in range(len(privacies)) :
        days = 0
        term_alphabet = privacies[i][-1]
        c_year, c_month, c_day = privacies[i][0:-2].split('.')

        for term in terms :
            if term[0] == term_alphabet :
                days = int(term[2:])*28

        diff_year = int(t_year) - int(c_year)
        diff_month = int(t_month) - int(c_month)
        diff_day = int(t_day) - int(c_day)
        diff_days = (diff_year * 28 * 12) + (diff_month * 28) + diff_day

        if diff_days >= days :
            result.append(i+1)

    return result