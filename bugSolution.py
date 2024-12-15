def function_with_improved_error_handling(x):
    if not isinstance(x, (int, float)):
        return "Error: Input must be a number"
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"

#Improved error handling
result1 = function_with_improved_error_handling(5)  # Output: 2.0
result2 = function_with_improved_error_handling(0)  # Output: Error: Division by zero
result3 = function_with_improved_error_handling("hello")  # Output: Error: Input must be a number
result4 = function_with_improved_error_handling([1,2,3]) # Output: Error: Input must be a number