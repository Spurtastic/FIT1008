"""Unit Testing for Task 1 and 2"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '20/05/2020'
__since__ = '22/05/2020'

import unittest
from hash_table import LinearProbeHashTable
from dictionary import Statistics, Dictionary


def file_len(filename: str) -> int:
    """Calculates the number of lines in a given file"""
    with open(filename, encoding='UTF-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


class TestDictionary(unittest.TestCase):
    DEFAULT_TABLE_SIZE = 250727
    DEFAULT_HASH_BASE = 31
    DEFAULT_TIMEOUT = 10
    FILENAMES = ['english_small.txt', 'english_large.txt', 'french.txt']
    RANDOM_STR = 'FIT1008 is the best subject!'

    def setUp(self) -> None:
        """ Used by our test cases """
        self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)

    def test_init(self) -> None:
        """ Testing type of our table and the length is 0 """
        self.assertEqual(type(self.dictionary.hash_table), LinearProbeHashTable)
        self.assertEqual(len(self.dictionary.hash_table), 0)

    def test_load_dictionary_statistics(self) -> None:
        """ For each file, doing some basic testing on the statistics generated """
        statistics = Statistics()
        for filename in TestDictionary.FILENAMES:
            words, time, collision_count, probe_total, probe_max, rehash_count = statistics.load_statistics(
                TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE * 2, filename,
                TestDictionary.DEFAULT_TIMEOUT)
            self.assertGreater(words, 0)
            self.assertLess(time, TestDictionary.DEFAULT_TIMEOUT)
            # TODO: Add your own test cases here
            words, time, collision_count, probe_total, probe_max, rehash_count = statistics.load_statistics(
                TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE * 2, filename,
                TestDictionary.DEFAULT_TIMEOUT)
            # collision_count
            self.assertGreater(collision_count, 0, "collisions are not being counted")

            # probe_total
            self.assertGreater(probe_total, 0, "total probes are incorrect")

            # probe_max
            self.assertGreater(probe_max, 0, "probes_max values are incorrect")

            # rehash_count
            self.assertGreater(rehash_count, 0, "rehashes are not being recorded")


    def test_load_dictionary(self) -> None:
        """ Reading a dictionary and ensuring the number of lines matches the number of words
            Also testing the various exceptions are raised correctly """
        for filename in TestDictionary.FILENAMES:
            self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
            words = self.dictionary.load_dictionary(filename)
            lines = file_len(filename)
            self.assertEqual(words, lines, "Number of words should match number of lines")

        # TODO: Add your own test cases (consider testing exceptions being raised)

        # testing if the number of words in the file is equivalent to the number of lines in the file
        number_of_words = self.dictionary.load_dictionary("words.txt")
        number_of_lines = file_len("words.txt")
        self.assertEqual(number_of_words, number_of_lines, "words in the file must be equal to the lines in the file")

        # testing the time out error
        res =""
        self.dictionary = Dictionary(1, 25027)
        try:

            self.dictionary.load_dictionary("english_small.txt", 5)
        except TimeoutError:
            # print("error happened moving on")
            res = "Error function ran longer than limit"

        self.assertEqual(res, "Error function ran longer than limit", "time limit exceeded but function kept going" )

    def test_add_word(self) -> None:
        """ Testing the ability to add words """
        # TODO: Add your own test cases
        self.dictionary.add_word("hello")
        self.assertTrue(self.dictionary.find_word("hello"), "word not added correctly")



    def test_find_word(self) -> None:
        """ Ensuring both valid and invalid words """
        # TODO: Add your own test cases
        # for false assertions with respect to non existing words in the dictionary
        self.assertFalse(self.dictionary.find_word("hello"), "error in find_word returning True when it should not")

        # trying for errors concerning case sensitive addition of strings
        msg = ""
        try:
            self.dictionary.add_word("yerk")
            self.assertFalse(self.dictionary.find_word("Yerk"), "expected error, fncn should return True")
        except AssertionError:
            msg = "Error as expected, if the string is upper case or lower case the find_word will always return true"
            return msg

        self.assertEqual(msg, "Error as expected, if the string is upper case or lower case the find_word will always return true", "error function is returning False")

        # For true assertions for when a word is added to the dictionary.
        self.dictionary.add_word("word")
        self.assertTrue(self.dictionary.find_word("word"), "error in find_word, its returning False when it should not")

        self.dictionary.add_word("$%#:#")
        self.assertTrue(self.dictionary.find_word("$%#:#"), "error in find_word, its returning False when it should not")

    def test_delete_word(self) -> None:
        """ Deleting valid words and ensuring we can't delete invalid words """
        self.dictionary.load_dictionary('english_small.txt')
        table_size = len(self.dictionary.hash_table)
        with self.assertRaises(KeyError):
            self.dictionary.delete_word(TestDictionary.RANDOM_STR)
        self.assertEqual(len(self.dictionary.hash_table), table_size)

        self.dictionary.delete_word('test')
        self.assertEqual(len(self.dictionary.hash_table), table_size - 1)


if __name__ == '__main__':
    unittest.main()

