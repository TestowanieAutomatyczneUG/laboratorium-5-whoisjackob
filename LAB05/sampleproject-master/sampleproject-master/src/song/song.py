class Song():
    def __init__(self):
        self.file = open('song.txt', '+r')
        self.f = self.file.read().splitlines()

    def close(self):
        self.file.close()
