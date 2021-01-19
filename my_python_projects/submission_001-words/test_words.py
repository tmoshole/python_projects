import unittest
import word_processor

class  MyTestCase(unittest.TestCase):
    def test_convert_to_word_list(self):
        """this tests whether the convert_to_word_list function returns a list splited string in lower cases
        """
        results = ['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you']
        self.assertEquals(word_processor.convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?"), results)

    def test_words_longer_than(self):
        """this tests whether the function only returns words longer than a specified length.
        """
        results = ['interesting', 'understatement']
        self.assertEquals(word_processor.words_longer_than(10,"These are indeed interesting, an obvious understatement, times. What say you?"),results)
    
    def test_words_lengths_map(self):
        """tests that the words_lengths_map function returns a dictionary that maps the number of words in a text.
        """
        results = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEquals(word_processor.words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?"),results)

    def test_letters_count_map(self):
        """this tests that the function returns a dictionary that maps each alphabet letter a to z 
            to the number of times that letter occurs in the text.
        """
        results = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEquals(word_processor.letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?"),results)

    def test_most_used_character(self):
        """this tests that the funtion returns the letter that occures the most in a text of string.
        """
        results = 'e'
        self.assertEquals(word_processor.most_used_character("These are indeed interesting, an obvious understatement, times. What say you?"),results)
