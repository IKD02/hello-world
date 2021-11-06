import sys
import socket


def hello_world() -> str:
    """
    Function that builds a message string, which introduces
    the PC (hostname) and its python version to the world.
    If python version is less than 3.6, the message indicates
    that f strings can't be used and is sad (since f strings were
    introduced at 3.6).

    @Returns (str): built message
    """
    message = "Hello world!"
    if sys.version_info.major >= 3 and sys.version_info.minor >= 6:
        message += f"\n\nI'm {socket.gethostname()} using python {sys.version_info.major}.{sys.version_info.minor} :)"
    else:
        message += "\n\nI'm {socket.gethostname()} using a python version older than 3.6 so I can't use f strings. :-("
    return message


if __name__=="__main__":
    print(message)
