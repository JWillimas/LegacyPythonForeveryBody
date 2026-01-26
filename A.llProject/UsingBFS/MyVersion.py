def gen_parentheses(pairs):
    if not isinstance(pairs,int):
        print("This not int")
    if pairs<1:
        print("Please input right num")
    
    queue=[("",0,0)]
    result=[]

    while queue:
        current,open_used,closed_used=queue.pop(0)
        if len(current)==2*pairs:
            result.append(current)
        
        if open_used<pairs:
            queue.append((current+"(",open_used+1,closed_used))
        if open_used>closed_used:
            queue.append((current+")",open_used,closed_used+1))

    print (result)
    return 

gen_parentheses(3)