def square_root_bisection(square_target, tolerance=1e-6, max_iterations=100):
    # Negative number check
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    # Handle 0 and 1
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # Set search bounds
    low = 0
    high = max(1, square_target)
    #make sure the search rang always contain 
    #the square root:
    #if 0<square_target<1 for example:0.25
    #√0.25 = 0.5 ,then [0,0.25]not include 0.5

    for _ in range(max_iterations):
        mid = (low + high) / 2
        squared = mid * mid
        error = abs(mid - square_target**0.5)

        # Check tolerance
        if error <= tolerance:
            print(
                f"The square root of {square_target} is approximately {mid}"
            )
            return mid

        # Adjust bounds
        if squared < square_target:
            low = mid
        else:
            high = mid

    # Failure case
    print(f"Failed to converge within {max_iterations} iterations")
    return None

print(square_root_bisection(0.001, 1e-7, 50))

