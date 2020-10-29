__author__ = "Ashwin Sarith"

from hash_table import LinearProbeHashTable
from dictionary import Dictionary
from list_adt import ArrayList
from enum import Enum
from typing import Tuple
from string import punctuation
import sys

from referential_array import ArrayR


# NOTE: below code is a modified version of the one found in FIT1045
def partition(array: ArrayR, begin: int, end: int):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MISSPELT = 3


class Frequency:
    def __init__(self) -> None:
        self.hash_table = LinearProbeHashTable()
        self.max_occurrence = 0
        self.dictionary = Dictionary(25027, 1000081)
        self.dictionary.load_dictionary("english_large.txt")
        self.max_words = (None, 0)

    def add_file(self, filename: str) -> None:
        """
        adds the words in the file to a list to be stripped of punctuation as well as be brought down to being lowercase
        :param filename:
        :return:
        :complexity: O(m*n) this entails the enumeration of each words as well as the iteration through each word in the text
        """
        mt_lst = []
        with open(filename, "r", encoding='UTF-8') as file:
            line = file.readline()
            while line:
                line = line.rstrip().split()
                mt_lst += line
                line = file.readline()
            # print(mt_lst)
            for word in mt_lst:

                # first set everything to lower case
                word_key = word.lower()

                # remove punctuation
                word_key = word_key.strip(punctuation + ",“”")
                # add the word if it exists in the dictionary instance in the __init__ method
                if self.dictionary.find_word(word_key):
                    if word_key in self.hash_table:
                        self.hash_table[word_key] += 1
                    else:
                        self.hash_table[word_key] = 1

                    # check and see if the word_key is greater than the current max occurences which is 0
                    if self.hash_table[word_key] > self.max_occurrence:
                        # if it is then set max occurence to the new value
                        self.max_occurrence = self.hash_table[word_key]

                        # then record the count as per the guideline (word, freq)
                        self.max_words = (word_key, self.max_occurrence)
        # print(self.max_words)
        file.close()

    def rarity(self, word: str):
        """

        :param word:
        :return:
        :complexity: will be O(1) since there are no loops
        """
        if word not in self.hash_table:
            return Rarity.MISSPELT
        # only will execute if the word inputted isnt something random
        data = self.hash_table[word]
        # if data is within a certain range then its something
        max = int(self.max_occurrence)
        if data >= (max / 100):
            return Rarity.COMMON
        elif (max / 100) <= data <= (max / 1000):
            return Rarity.UNCOMMON
        else:
            return Rarity.RARE

    def ranking(self) -> ArrayList[tuple]:
        """
        the words are copied to an Array list to be further iterated and sorted using quicksort
        :return:
        """
        arr = ArrayList(len(self.hash_table))
        hash_table = self.hash_table.get_table()
        file_length = len(hash_table)
        index = 0
        while index < file_length - 1:
            if hash_table[index] not in [None]:
                arr.append(hash_table[index])
                index += 1
            else:
                index += 1
        sys.setrecursionlimit(10000)
        quick_sort(arr)
        return arr


def frequency_analysis() -> None:
    stat = Frequency()
    stat.add_file("215-0.txt")
    words_ranks = stat.ranking()
    while True:
        usr_input = int(input("number of your choice thats greater than 0 only input 0 to quit"))
        try:
            assert usr_input >= 0, "incorrect input"
        except AssertionError:
            print("incorrect input try again")
            continue
        for i in range(usr_input):
            rare = stat.rarity(words_ranks[i][0])
            print("rank" + str(i + 1) + "word" + words_ranks[i][0] + "Rarity" + str(rare))

        if usr_input == 0:
            break


if __name__ == '__main__':
    frequency_analysis()
