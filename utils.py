import re

is_username = lambda username: bool(re.fullmatch(r"^[a-zA-Z0-9_.+-]+$", username, flags=re.I))

def is_email(string: str) -> bool:
    regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(regex_email, string, flags=re.I))


def ensure_email(string: str) -> str:
    if is_email(string): return string
    if is_username(string): return f"{string}@yopmail.com"
    raise RuntimeError(f"Could not construct email from data {string} only letters, numbers and _.+- symbols can be used")


def is_usrId(string: str) -> bool:
    return bool(re.fullmatch(r"\w+-\d\d\d-\d+", string, flags=re.I))

