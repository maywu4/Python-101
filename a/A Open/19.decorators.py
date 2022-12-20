def exponent_function_decorator(exponent_function_to_wrap):
    def wrapper_function(base_number, exponent):
        return base_number ** exponent_function_to_wrap(exponent)
    return wrapper_function

def exponent_function(exponent):
    return int(exponent)
