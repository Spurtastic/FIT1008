"""Unit Testing for Task 3 and 4"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '30/05/2020'
__since__ = '22/05/2020'

import unittest
import sys
from hash_table import LinearProbeHashTable
from frequency import Frequency, Rarity



class TestFrequency(unittest.TestCase):
    def setUp(self) -> None:
        self.frequency = Frequency()

    def test_init(self) -> None:
        # TODO: Add 3 or more unit tests
        self.assertEqual(self.frequency.max_occurrence, 0, "max occurrences initialised incorrectly")
        self.assertEqual(self.frequency.max_words, (None, 0) , "max_word initialised incorrectly")
        self.assertEqual(type(self.frequency.hash_table), LinearProbeHashTable, "error hash is not initialised using Linear probe")

    def test_add_file(self) -> None:
        # TODO: Add 3 or more unit tests
        self.frequency.add_file("215-0.txt")

        # ensure that the file is loaded by checking if there are changes in the hash_tables
        self.assertGreater(len(self.frequency.hash_table),0)


    def test_rarity(self) -> None:
        # TODO: Add 3 or more unit tests
        self.frequency.add_file("215-0.txt")
        self.assertEqual(self.frequency.rarity("tilda"), Rarity.MISSPELT, "Rarity applied incorrectly")
        self.assertEqual(self.frequency.rarity("the"), Rarity.COMMON, "Rarity applied incorrectly")
        self.assertEqual(self.frequency.rarity("nomadic"), Rarity.RARE, "Rarity applied incorrectly")


if __name__ == '__main__':
    unittest.main()

