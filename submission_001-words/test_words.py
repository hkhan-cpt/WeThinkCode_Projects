import unittest
import word_processor
from word_processor import *


class MyTests(unittest.TestCase):
    def test_step1(self):
        """Checks that the string of text is returned as a list of lowercase strings.
        """
        result = convert_to_word_list("What is happening on Tuesday? Tell me, now!")
        self.assertEqual(["what", "is", "happening","on","tuesday","tell","me","now"], result)


    def test_step1_blank_string(self):
        """Checks that a blank string is returned as an empty list.
        """
        result = convert_to_word_list("")
        self.assertEqual([], result)


    def test_step2(self):
        """Checks that only words longer than the specified length are returned, in a list.
        """
        result = words_longer_than(3, "What is happening on Tuesday? Tell me, now!")
        self.assertEqual(["what", "happening", "tuesday", "tell"], result)


    def test_step2_blank_string(self):
        """Checks that a blank string is returned as an empty list.
        """
        result = words_longer_than(5, "")
        self.assertEqual([], result)


    def test_step2_empty_result(self):
        """Checks that an empty list is returned if there are no words longer than the specified length.
        """
        result = words_longer_than(50, "What is happening on Tuesday? Tell me, now!")
        self.assertEqual([], result)


    def test_step3(self):
        """Checks that the string of text is returned as a dictionary where word lengths are mapped to the number of times a word of that length appears in the text.
        """
        result = words_lengths_map("What is happening on Tuesday? Tell me, now!")
        self.assertEqual({2: 3, 3: 1, 4: 2, 7: 1, 9: 1}, result)


    def test_step3_blank_string(self):
        """Checks that a blank string is returned as an empty list.
        """
        result = words_lengths_map("")
        self.assertEqual({}, result)


    def test_step4(self):
        """Checks that a string of text is returned as a dictionary with all letters mapped to the number of times it 
        appears in the text.
        """
        result = letters_count_map("What is happening on Tuesday? Tell me, now!")
        self.assertEqual({'a': 3, 'b': 0, 'c': 0, 'd': 1, 'e': 4, 'f': 0, 'g': 1,
         'h': 2, 'i': 2, 'j': 0, 'k': 0, 'l': 2, 'm': 1,'n': 4, 'o': 2, 'p': 2, 'q': 0,
         'r': 0, 's': 2, 't': 3, 'u': 1, 'v': 0, 'w': 2, 'x': 0, 'y': 1, 'z': 0}, result)


    def test_step4(self):
        """Checks that a blank string is returned as a dictionary with all letters mapped to zero.
        """
        result = letters_count_map("")
        self.assertEqual({'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
         'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0,
         'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}, result)


    def test_step5(self):
        """Checks that the character which appears the most times in the text is returned.
        """
        result = most_used_character("What is happening on Tuesday? Tell me, now!")
        self.assertEqual("e", result)


    def test_step5_blank_string(self):
        """Checks that a blank string is returned as None.
        """
        result = most_used_character("")
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()