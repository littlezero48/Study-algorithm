def solution(cacheSize, cities):
    
    if cacheSize == 0 :
        return len(cities) * 5
    
    cache_list = []
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache_list:
            time += 1
            cache_list.append(cache_list.pop(cache_list.index(city)))
        else :
            time += 5

            if len(cache_list) < cacheSize :
                cache_list.append(city)
            else :
                cache_list.pop(0)
                cache_list.append(city)

    return time