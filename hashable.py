class alphabet:
    def __init__(self, c):
        self.char = c

    def __hash__(self):
        return ord(self.char)

