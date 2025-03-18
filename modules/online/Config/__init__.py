import os

from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

ENV = bool(os.environ.get("ENV", False))

if ENV or os.path.exists(".env"):
    from vars import *  # noqa
elif os.path.exists("vars.py"):
    from vars import *  # noq
