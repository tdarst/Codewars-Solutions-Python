def solution(string,markers):
    
    split = string.split('\n')
    
    if markers:
        for x in range(0,len(split)):
            for y in markers:
                if y in split[x]:
                    split[x] = split[x][:split[x].find(y)]
                split[x] = split[x].strip()
                
        return '\n'.join(split)
    
    else:
        for x in range(0,len(split)):
            split[x] = split[x].strip()
            
        return '\n'.join(split)