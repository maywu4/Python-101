def exponent_function_decorator(exponent_function_to_wrap):
    def wrapper_function(base_number, exponent):
        return base_number ** exponent_function_to_wrap(exponent)
    return wrapper_function

@exponent_function_decorator
def exponent_function(exponent):
    return int(exponent)

# print(exponent_function)
print(exponent_function(4, 2.23746))
# exponent_function = exponent_function_decorator(exponent_function)
# print(exponent_function)
# print(exponent_function._closure_[0].cell_contents)

