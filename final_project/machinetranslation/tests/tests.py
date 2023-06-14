import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertEqual(english_to_french("butterfly"), "papillon") 
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("bonjour"), "hello") 
        self.assertEqual(french_to_english("papillon"), "butterfly") 
        
unittest.main()
