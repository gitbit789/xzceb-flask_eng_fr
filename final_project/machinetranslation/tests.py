"""Language Translator Test Module"""
import unittest
from translator import english_to_french, french_to_english

class Testenglishtofrench(unittest.TestCase):
    """Testenglishtofrench"""
    def test1(self):
        """test1"""
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class Testfrenchtoenglish(unittest.TestCase):
    """Testfreshtoenglish"""
    def test2(self):
        """test2"""
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        