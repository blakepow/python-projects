class Song:
    def __init__(self, name = 'unknown', genre = 'unknown'):
        self.name = name
        self.genre = genre

    def get_name(self, name):
        return self._name