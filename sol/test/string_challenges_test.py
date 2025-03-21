import unittest
import sys
from pathlib import Path
import sys
import os

# Ensure the correct path is added to be able to import local modules
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# print(f"Added path: {SRC_PATH}")
import string_challenges as sln

class TestStringChallenges(unittest.TestCase):

    def test_sol_0(self):
        self.assertEqual(5, sln.convert_string_to_num_bytes("café"))
        self.assertEqual(2, sln.convert_string_to_num_bytes("hi"))
        self.assertEqual(0, sln.convert_string_to_num_bytes(""))
        self.assertEqual(1, sln.convert_string_to_num_bytes("a"))
        self.assertEqual(2, sln.convert_string_to_num_bytes("à"))

    def test_sol_1(self):
        self.assertEqual(set(['https://pythonidae.herokuapp.com/web/generate',
                            'https://pythonidae.herokuapp.com/web/identify',
                            'https://pythonidae.herokuapp.com/web/cookies']), 
                            set(sln.concatenate_string_to_each_element('https://pythonidae.herokuapp.com/', ['web/generate', 'web/identify', 'web/cookies'])))
    
    def test_sol_2(self):
        self.assertEqual(sln.conceal_substring('MII CyberSec Consulting Service', 4, 11), 'MII xxxxxxxx Consulting Service')
        self.assertEqual(sln.conceal_substring('Very Sensitive Information: abcdefg', 26, 32), 'Very Sensitive Information: xxxxxxx')



if __name__ == '__main__':
    unittest.main()
