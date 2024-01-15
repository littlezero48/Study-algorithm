from itertools import permutations

def isPrime(num) :                          # 소수 판별 함수
    if num <= 1 :                           # 1,0 경우 소수가 아님
        return False
    for i in range(2, int(num ** 0.5) + 1): # 2부터 Num의 제곱근 사이에서 한번이라도 나눠 떨어진다면 소수가 아님
        if num % i == 0 :
            return False
    return True                             # 이 모든 상황에서 제외된다면 소수


def solution(numbers):
    answer = 0
    nums = [ n for n in numbers ]           # numbers의 숫자를 리스트
    permu = []                              # 순열 조합을 담을 리스트
    prime_nums = []                         # 소수
        
    # 서로 다른 n개에서 m개를 선택해 순서있게 나열하여 숫자를 만드는 것이므로 순열 개념 사용
    for j in range(1, len(numbers)+1):
        permu += list(permutations(nums, j))            # numbers가 17인 경우는 이렇게 [('1',), ('7',), ('1', '7'), ('7', '1')]
    
    # 다차원 배열로 된 값을 하나의 값으로 조합하고 숫자로 변한
    comb_nums = [int(("").join(k)) for k in permu]      # [1, 7, 17, 71]
    
    comb_nums = list(set(comb_nums))                    # 중복 수 제거
        
    for l in comb_nums :
        if isPrime(l) :
            answer += 1
        
    return answer