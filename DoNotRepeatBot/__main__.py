"""
Starts the bot.
"""

import sys
from .server import Server

server = Server()

if "-p" in sys.argv:
    server.poll()
else:
    server.listen()
