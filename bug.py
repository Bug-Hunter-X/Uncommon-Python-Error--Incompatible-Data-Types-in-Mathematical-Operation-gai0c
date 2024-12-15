def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"

# Uncommon error: Using a non-numeric type in a mathematical operation
result1 = function_with_uncommon_error(5)  # Output: 2.0
result2 = function_with_uncommon_error(0)  # Output: Error: Division by zero
result3 = function_with_uncommon_error("hello")  # Output: Error: Invalid input type
result4 = function_with_uncommon_error([1,2,3]) # Output: Error: unsupported operand type(s) for /: 'int' and 'list'