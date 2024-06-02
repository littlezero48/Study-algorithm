from itertools import permutations 

def solution(k, dungeons):    
	dun_cnt_list = []     
	
	for perm in permutations(range(len(dungeons)), len(dungeons)):         
		temp_k = k        
		dun_cnt = 0            
		for i in perm:            
			need_k, use_k = dungeons[i]                  
			if temp_k >= need_k:                
				dun_cnt += 1                
				temp_k -= use_k             
			dun_cnt_list.append(dun_cnt)  
			
	return max(dun_cnt_list)