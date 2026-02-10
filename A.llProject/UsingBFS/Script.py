def gen_parentheses(pairs):
    #judge the input element
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    #Unpacking the tuple from queue 
        #Loop through it : by three parameters to operate the parentheses-draw
            #pair(global-variable),open_used,closed_used(accumulate-variables)
    queue = [('', 0, 0)]
    result = []
    while queue:
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result
print(gen_parentheses(2))

