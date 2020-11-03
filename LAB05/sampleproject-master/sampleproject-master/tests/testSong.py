import unittest
import song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = song.Song()

    def tearDown(self):
        self.song.close()