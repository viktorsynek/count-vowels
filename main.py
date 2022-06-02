import unittest

def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels:
            count+= 1
    
    return count

class Test(unittest.TestCase):
    def test_with_my_first_name(self):
        self.assertEqual(vowel_count("test"), 1)
    # true = passed

    def test_with_my_last_name(self):
        self.assertEqual(vowel_count("toast"), 1) # change to 2 to both pass
    # false = failed
   