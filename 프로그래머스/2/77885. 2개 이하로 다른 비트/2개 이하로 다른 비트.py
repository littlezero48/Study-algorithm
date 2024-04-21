def solution(numbers):
    answer = []

    for number in numbers:
        # 숫자가 짝수면 마지막 비트가 0 이므로 1을 더해주면 
        # x보다 큰수가 되고, 다른 비트의 개수 또한 2개 이하인 1개가 되며, 2개 이하 다른 비트 중 가장 작은 수 
        # 주어진 세가지 모든 조건에 충족되기 때문에 +1 해주는 것으로 답이 나온다
        if number % 2 == 0:
            answer.append(number + 1)
            continue

        # 숫자가 홀수면
        # 일단 주어진 x보다 커야한다는 조건 때문에 맨 뒤에서부터 숫자를 바꾸는 것이 아닌
        # 현재 이진수 중 가장 마지막에 있는 0 비트를 1로 바꾸어주고 그 다음 비트를 0으로 바꿔주면  
        # 01XXXX > 10XXXX 가 되면서 
        # x보다는 크고, 다른비트의 개수는 2개 이하이며, 다른비트의 개수 2개 이하의 수 중 가장 작은 수에 해당하게 된다.
        
        # 이진수를 이진수 문자열로 바꾸고 이진수라는 걸 표기하는 0b를 제외
        # 그리고 마지막 0비트를 찾아야하는데 binary문자열로 바꾼 경우 0이 없을 경우를 대비해 앞에 0을 추가
        number_bin = '0' + bin(number)[2:] 
        # 가장 마지막 0비트의 위치 전까지 문자열을 잘라내고, 
        # 마지막 0 > 1 그 다음을 0 으로 바꾼 문자열을 더하고 이 2개 문자열 자리만큼을 제외한 그 뒤 나머지를 붙인다
        # 이를 다시 숫자화
        number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0') + 2:]       
        answer.append(int(number_bin, 2))

    return answer