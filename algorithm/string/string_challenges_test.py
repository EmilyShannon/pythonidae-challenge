import unittest
from string_challenges import StringChallengeSolution 

class TestStringChallenges(unittest.TestCase):
    def setUp(self):
        self.sln = StringChallengeSolution()

    def test_sol_0(self):
        self.assertEqual(5, self.sln.convert_string_to_num_bytes("café"))
        self.assertEqual(2, self.sln.convert_string_to_num_bytes("hi"))
        self.assertEqual(0, self.sln.convert_string_to_num_bytes(""))
        self.assertEqual(1, self.sln.convert_string_to_num_bytes("a"))
        self.assertEqual(2, self.sln.convert_string_to_num_bytes("à"))

    def test_sol_1(self):
        self.assertEqual(set(['https://pythonidae.herokuapp.com/web/generate',
                            'https://pythonidae.herokuapp.com/web/identify',
                            'https://pythonidae.herokuapp.com/web/cookies']), 
                            set(self.sln.concatenate_string_to_each_element('https://pythonidae.herokuapp.com/', ['web/generate', 'web/identify', 'web/cookies'])))

if __name__ == '__main__':
    unittest.main()
