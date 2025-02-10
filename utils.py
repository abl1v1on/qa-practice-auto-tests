import os


def disable_proxy() -> None:
    os.system('proxy -d')


def enable_proxy() -> None:
    os.system('proxy -e')
