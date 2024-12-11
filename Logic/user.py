import os
from pathlib import Path
from settings import logging, Logger


class User:
    def __init__(self, username, medium="Unknown"):
        volume_path = os.getenv("VOLUME") or Path.cwd()  # TODO ?????
        username = username if username else "[BASIC_USER]"
        self.name = username
        self.accounts_list_file = (volume_path / "accounts" / f"{username}.txt")
        # check if user exists
        if not self.accounts_list_file.exists():
            Logger("[BASIC_USER]", level=logging.DEBUG).info(f"First login for [{username}] user.")
            self.accounts_list_file.touch()
        self.log = Logger(username, level=logging.DEBUG)
        self.log.info(f"Login in to the account via {medium}")
        self.add_account = Logger(username, type="account", level=logging.INFO).info

    def is_basic_user(self):
        return self.name == "[BASIC_USER]"

    def get_the_account_list(self):
        with open(self.accounts_list_file, "r") as file:
            return list(map(str.strip, file.readlines()))
