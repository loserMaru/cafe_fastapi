def parse_error_message(error_detail):
    error_type = error_detail["type"]
    if error_type == "string_too_short" and error_detail["loc"][-1] == "password":
        return "Password is too short"
    elif error_type == "value_error.email":
        return "Invalid email format"
    else:
        return "Validation error"
