import re

is_username = lambda username: bool(re.fullmatch(r"^[a-zA-Z0-9_.+-]+$", username, flags=re.I))

