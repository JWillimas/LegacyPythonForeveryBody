def square_root_bisection(squr_target,tolerance=1,iteration=1):
    
    if squr_target<0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if (squr_target==0) or (squr_target==1):
        print(f"The square root of {squr_target} is {squr_target}")
        return squr_target

    low=0
    high=max(1,squr_target)

    for _ in range(iteration):
        squr_root_mid=(low+high)/2

        result_mid=squr_root_mid*squr_root_mid

        error=abs(result_mid-squr_target)

        if error<=tolerance:
            print(f"The square root of {squr_target} is approximately {squr_root_mid}")
            return squr_root_mid
        
        if result_mid>squr_target:
            high=squr_root_mid
        
        else:
            low=squr_root_mid
    
    print(f"Failed to converge within the {iterations} iterations ")
    return None

print(square_root_bisection(0.001, 1e-7, 50))