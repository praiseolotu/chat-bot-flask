import unittest
from translate import translator

class TestTranslateEnToFr(unittest.TestCase):
   
    def test1(self):
        
        self.assertIsNone(translator.english_to_french(None))
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Bonjour"), "Hello")

class TestTranslateFrToEn(unittest.TestCase):
    self):
        
        self.assertIsNone(translator.french_to_english(None))
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Hello"), "Bonjour")

unittest.main()
