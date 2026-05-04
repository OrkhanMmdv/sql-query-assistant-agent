def validate_user_input(user_input):
    if user_input is None:
        return False

    if len(user_input.strip()) == 0:
        return False

    return True