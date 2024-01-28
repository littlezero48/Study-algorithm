def solution(number, k):
    # 숫자 제거하고 나머지 숫자는 위치가 변하지 않은 상태에서 가장 큰 숫자를 찾는것
    answer = []   

    for i in number:
        # 1) 빠져야할 숫자가 남아있으면
        # 2) answer에 숫자가 있다면
        # 3) answer의 마지막 값이 i보다 작다면
        while  k > 0 and answer and answer[-1] < i :
            # 숫자를 pop해 제거하고
            answer.pop()
            # 숫자를 제거했으니 빼야할 숫자 개수를 줄인다.
            k -= 1
        # 그 외에는 answer 값에 추가
        answer.append(i)
        

        
    # 만약 위에서 k를 모두 제거했다면 k=0 이겠지만, 모두 같은 수등의 예외가 있다면 k는 하나도 제거되지 않은채 여기까지 도달함
    # 따라서 제거되지 않은 숫자 나머지를 답변 전에 answer 길이에서부터 k를 빼 제거하여 큰수를 생성
    # len(answer)-k를 하는 이유는 그냥 -k를 하게되면 0 경우 값이 출력이 안됨
    return ''.join(answer[:len(answer)-k])