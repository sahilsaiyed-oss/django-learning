import re


def validate_username(username):
    """
    Validates username:
    - Minimum 4 characters
    - Only letters, numbers, underscores allowed
    """

    if len(username) < 4:
        raise ValueError("Username must be at least 4 characters long.")

    pattern = r"^[a-zA-Z0-9_]+$"
    if not re.match(pattern, username):
        raise ValueError("Username can only contain letters, numbers, and underscores.")

    return username


def validate_password_strength(password):
    """
    Validates password strength:
    - Minimum 8 characters
    - At least 1 uppercase
    - At least 1 lowercase
    - At least 1 digit
    """

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit.")

    return password


def sanitize_input(text):
    """
    Basic sanitization to prevent unwanted characters.
    """

    cleaned = re.sub(r"[<>]", "", text)
    return cleaned.strip()
