# 대문자와 소문자를 구분하므로
# 샵이 붙는 음은 소문자 하나로 바꾸어 처리하기 쉽게 만든다, 아니면 기존 문자랑 겹치지 않는 다른 문자로도 가능
def get_chord(chord):
    chord = (
        chord.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
    )    
    return chord

# 문자열로 되어 있는 시간을 시간으로 변환 
def get_time(time):   
    hour, minuite = map(int, time.split(':'))
    return hour * 60 + minuite
    
def solution(m, musicinfos):
    answer = ''    
    m_chord = get_chord(m)
    m_index = 0
    m_list = []
    
    for musicinfo in musicinfos :
        start, end, name, chord = musicinfo.split(",")
        
        # 단위가 분 기준임 12:14 이면 12시 14분.
        play_time = get_time(end) - get_time(start)
        chord = get_chord(chord)
        
        # 주의: 3번째 조건, 각음은 1분에 1개. 음악 < 재생 경우, 처음부터 반복 / 음악 > 재생 경우, 재생 시간만큼만
        # 코드 길이와 시간을 대조하여 반복하고 나머지 시간 만큼 일부를 가져와야함
        full_chord = chord * (play_time // len(chord)) + chord[:(play_time % len(chord))]
        
        # 네오가 기억한 멜로디와 대조
        if m_chord in full_chord :
            m_list.append([play_time, m_index, name]) # play_time이 같은 경우 m_index로 정렬해야하기 때문
            m_index += 1
        
    # 일치하는 곡이 한개 이상이라면
    if len(m_list) > 1 :
        # 1순위 플레이시간, 2순위 먼저 입력된 순 으로 정렬 후 가장 처음 0 인덱스에 있는 노래 제목을 출력
        answer = sorted(m_list, key=lambda x: (-x[0], x[1]))[0][2] 
    elif len(m_list) == 1 :
        answer = m_list[0][2]
    else :
        answer = "(None)"
           
    return answer