# tests/test_main.py
import unittest
from py_morse.main import text_to_morse, morse_to_text

class TestMorseCodeConversion(unittest.TestCase):

    def test_text_to_morse(self):
        self.assertEqual(text_to_morse('SOS'), '... --- ... ')
        self.assertEqual(text_to_morse('Hello'), '.... . .-.. .-.. --- ')

    def test_morse_to_text(self):
        self.assertEqual(morse_to_text('... --- ...'), 'SOS')
        self.assertEqual(morse_to_text('.... . .-.. .-.. ---'), 'HELLO')

if __name__ == '__main__':
    unittest.main()
