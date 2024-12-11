import logging
import os
import tomllib
from pathlib import Path


def load_settings():
    with open("../settings.toml", "rb") as file:
        settings = tomllib.load(file)
        print(settings["countries"]["Z1"])


class Logger(logging.Logger):
    def __init__(self, username="System", filename=None, type="user", level=logging.NOTSET):
        volume_path = os.getenv("VOLUME") or Path.cwd()  # TODO ?????
        super().__init__(username, level)

        match type:
            case "user":
                # filename = filename or (volume_path / "logs" / "user" / f"{username}.log")
                filename = filename or (volume_path / "logs" / f"User.log")
                formatter = logging.Formatter('%(asctime)s::%(levelname)8s::%(name)s::%(message)s', "%Y-%m-%d %H:%M:%S")
            case "account":
                filename = filename or (volume_path / "accounts" / f"{username}.txt")
                formatter = logging.Formatter('%(message)s')
            case "system":
                filename = filename or (volume_path / "logs" / f"System.log")
                formatter = logging.Formatter('%(asctime)s::SYSTEMS::%(levelname)8s::%(message)s', "%Y-%m-%d %H:%M:%S")
            case "requests":
                filename = filename or (volume_path / "logs" / f"System.log")
                formatter = logging.Formatter('%(asctime)s::REQUEST::%(levelname)8s::%(message)s', "%Y-%m-%d %H:%M:%S")
            case _:
                filename = filename or (volume_path / "logs" / f"logs of unknown type.log")
                formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s', "%Y-%m-%d %H:%M:%S")

        # Add handlers (e.g., ConsoleHandler, FileHandler, etc.)
        handler = logging.FileHandler(filename=filename)
        handler.setFormatter(formatter)
        self.addHandler(handler)
