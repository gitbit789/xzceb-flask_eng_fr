import unittest
from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    """
    Unit test for English To French translator
    """
    def test1(self):
        """
        Test Hello to Bonjour
        """
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test2(self):
        """
        Test null 
        """
        self.assertNotEqual(englishToFrench(""), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Unit test for French to English translator
    """
    def test1(self):
        """
        Test Bonjour to Hello
        """
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test2(self):
        """
        Test null
        """
        self.assertNotEqual(frenchToEnglish(""), "Hello")

unittest.main(verbosity=3)
        
