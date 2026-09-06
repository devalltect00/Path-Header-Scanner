# app/cli/constants/enums.py

from enum import Enum


class LogLevelChoices(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            value = value.upper()
            for member in cls:
                if member.value == value:
                    return member


class CleanupTypeChoices(str, Enum):
    ALL = "all"
    COMMIT = "commit"
    TAG = "tag"
    BRANCH = "branch"


class InitMode(str, Enum):
    ALL = "all"
    CONFIG = "config"
