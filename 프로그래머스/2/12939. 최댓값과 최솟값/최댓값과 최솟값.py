def solution(s):
    # s열은 문자열이므로 그 상태로 배열을 만들어서 min, max를 해봐도 아스키 코드값에 의해 최소값과 최대값을 찾는다
    # 따라서 숫자로써 최소값가 최대값을 찾으려면 int로 형변환했다가 출력할때는 문자열로 바꾸는 과정이 필요하다
    s_arr = list(map(int , s.split(" "))) 
    return str(min(s_arr)) + " " + str(max(s_arr))