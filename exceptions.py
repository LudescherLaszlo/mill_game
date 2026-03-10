class MillException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class InvalidMoveException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class RemovePeaceException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class PlacePeaceException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class MovePeaceException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class GameOverException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
class JumpPeaceException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message