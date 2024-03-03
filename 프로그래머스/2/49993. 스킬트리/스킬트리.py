# skill = 선행 스킬
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        s = ''
        for i in tree:      
            # 스킬트리안 스킬을 선행스킬과 관련된 것만으로 정리하는 과정 
            # (여기서 스킬 트리와 상관 없이 배울 수 있는 스킬은 검증 대상에서 제외되고 해당 스킬들만 정리)
            if i in skill:  
                s += i
        
        # 선행 스킬에서 정리된 스킬트리와 대조했을때 같다면 습득 가능한 스킬트리 이므로 +1
        if skill[:len(s)] == s: 
            answer += 1  
            
    return answer