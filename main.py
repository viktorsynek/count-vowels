############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import unittest

def vowel_count(string):
    # ALL THE VOWELS IN ONE LIST
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    # LOOP THROUGH THE GIVEN STRING
    for i in string:
        # IF THE CHARACTER IS INSIDE THE VOWELS LIST 
        # MEANING THE CHARACTER IS A VOWEL
        if i in vowels:
            # ADD ONE TO THE VOWEL COUNTER
            count+= 1
    
    return count

class Test(unittest.TestCase):
    def test_with_my_first_name(self):
        self.assertEqual(vowel_count("test"), 1)
    # true = passed

    def test_with_my_last_name(self):
        self.assertEqual(vowel_count("toast"), 1) # change to 2 to both pass
    # false = failed
   
