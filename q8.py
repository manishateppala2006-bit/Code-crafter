def sanitize_email(raw_input: str) -> str:
    s = raw_input.strip().lower()
    return s if s and s.count("@") == 1 else "Invalid Email"
