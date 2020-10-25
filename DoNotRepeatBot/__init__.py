"""
DoNotRepeat is a bot that allows you to send messages without you having to repeat it.
"""

import logging
from .server import Server

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO,
)
