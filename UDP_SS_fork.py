#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
from socketserver import DatagramRequestHandler, ForkingUDPServer


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


class UpperHandler(DatagramRequestHandler):
    def handle(self):
        print("New request: {}".format(self.client_address))
        msg = self.rfile.read()
        self.wfile.write(upper(msg))


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

server = ForkingUDPServer(('', int(sys.argv[1])), UpperHandler)
server.serve_forever()
