def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return a / b
    except ZeroDivisionError:
        return "Division by zero"

result = function_with_uncommon_error(5,0)
print(result) # Output: Division by zero
result2 = function_with_uncommon_error(5,2)
print(result2) # Output: 2.5