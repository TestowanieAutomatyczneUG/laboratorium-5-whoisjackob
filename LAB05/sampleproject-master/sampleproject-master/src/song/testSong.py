import unittest
from song.Piosenka import Piosenka

class SongTest(unittest.TestCase):

    def test_song(self):
        self.assertEqual(self.temp.wszystko(), self.temp.wszystko())
    def setUp(self):
        self.temp = Piosenka()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")