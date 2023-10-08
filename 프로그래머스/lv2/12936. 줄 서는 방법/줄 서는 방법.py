import math
def solution(n, k):
    
    # 1 2 3
    # 1 3 2
    # 2 1 3
    # 2 3 1
    # 3 1 2
    # 3 2 1
    
    # n 명에게 번호를 붙여 리스트 업
    people = [i for i in range(1, n + 1)]
    result = [] 
    
    while n:
        # n명일때 줄을 서는 방법은 n!(factorial)에 해당 하고 이걸 n명으로 나누면 한명이 맨앞에 나왔을때의 가지 수가 된다.
        one_case = math.factorial(n) // n
        # 전체 경우 수 중에서 k번째니까 k를 한명의 경우의 수로 나누면 k번째가 몇번째 사람인지 알 수있다.
        people_num = k // one_case
        # k를 한명의 경우의 수로 나눈 나머지는 위에서 알게된 몇번째 사람의 몇번째 경우의 수인지 알 수있다.
        k %= one_case        
        if k == 0: result.append(people.pop(people_num - 1)) 
        else: result.append(people.pop(people_num))
            
        n -= 1 # 한명은 자리를 잡았으니 다음 번에 이 사람을 제외하고 자리잡도록 한명 제외
        
    return result