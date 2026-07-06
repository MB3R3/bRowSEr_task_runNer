import sys


class CLI:

    def __init__(self):
        self.command = None

    def get_command(self):
        if len(sys.argv) < 2:
            return None
        
        return sys.argv[1].lower()