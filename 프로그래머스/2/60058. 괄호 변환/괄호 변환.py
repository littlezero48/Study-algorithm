def Balance_check(s):
    check = 0
    for i in s:
        if( i == '(' ):
            check +=1
        else :
            check -=1
    if ( check == 0 ) :
        return True
    else:
        return False

def Collect_check(s):
    l = []
    for i in s:
        if( i == '(') :
            l.append(i)
        else:
            if(len(l) == 0):
                return False
            else:
                l.pop()
        
    if(len(l) == 0):
        return True
    else :
        return False

def solution(p):
    answer = ''
    u = ""
    v = ""
    
    if( len(p) == 0 or Collect_check(p) ) :
        return p
    
    for i in range(2,len(p)+1,2) :
        if( Balance_check(p[0:i]) ) :
            u = p[:i]
            v = p[i:]
            break
    
    if( Collect_check(u) ):
        answer += u + solution(v)
    else :
        answer += '(' + solution(v) + ')'
        for i in u[1:-1]:
            if( i == '('):
                answer += ')'
            else:
                answer += '('
    
    return answer