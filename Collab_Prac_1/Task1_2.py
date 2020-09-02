""" Basic template for tasks 1 and 2.

Provides a base for students to practice creating robust, simple
algorithms, based on commenting then, determining their postconditions and
preconditions if any, and doing some extremely basic testing.

:func: sum_of_digits(x: int) -> int:
       sums the digits of non-negative integer x
:func: sum_digits_of_non_negatives(a_list: List[int]) -> List[int]:
       sums the digits of each non-negative int in a_list & returns them
:func: table_time(filename: str, threshold: int, lower: int, upper: int) -> None:
       Creates csv file and related pdf plots timing the above function
"""
__author__ = "Maria Garcia de la Banda, modified by Brendon Taylor"
__docformat__ = 'reStructuredText'

import timeit
import random
import csv_plotting
import os

from typing import List

random.seed(1)


def sum_of_digits(x: int) -> int:
    """ Computes the sum of the digits of non-negative integer x. 

    :pre: x is >= 0
    :raises ValueError: if x < 0
    """
    if x >= 0:
        sum = 0
        while x > 0:
            sum += x % 10
            x = x // 10 
        return sum
    else:
        raise ValueError("x must be >= 0")        




def __create_list(length: int, lower: int, upper: int) -> List[int]:
    """ Creates a list of given length where elements are random 
    integers within interval [upper, lower]. 

    :pre: lower <= upper
    :post: returned list has length elements within [upper,lower]
    """
    a_list = [0] * length
    for i in range(length):
        a_list[i] = random.randint(lower, upper)
    return a_list


def table_time(filename: str, threshold: int, lower: int, upper: int) -> None:
    """ Creates lists of increasing power-of-2 length, until threshold,
    where elements are random integers within [lower,upper] interval. 
    For each list, it calls sum_of_digits_of_non_negatives and writes
    a line in the comma separated filename, with the length of the list,
    and the times needed to create and process it. If threshold <= 2, it
    does nothing.

    :pre: lower <= upper 
    :raises ValueError: if lower > upper
    """
    length = 2
    if length < threshold: # file will not be empty
        file = open(filename, "w")
		
        while length < threshold:
            time_at_start = timeit.default_timer()
            a_list = __create_list(length,lower, upper)
            time_after_create = timeit.default_timer()
            time_to_create = time_after_create - time_at_start 
            sum_digits_of_non_negatives(a_list)
            time_after_sum = timeit.default_timer()
            time_to_sum = time_after_sum - time_after_create 
            file.write(str(length) + "," + str(time_to_create) + "," + str(time_to_sum) + "\n")
            length = length << 1
			
        file.close()
        csv_plotting.plot_csv(filename, 3)
        
def sum_digits_of_non_negatives(a_list: List[int]) -> List[int]:
    """ Computes a new list, summing the digits of each non-negative 
        element in a_list. 
    """
    new_list = []
    for item in a_list:
        try:
            sum = sum_of_digits(item)
        except ValueError:
            pass
        else:
            new_list.append(sum)
    return new_list


def __test_sum_of_digits():
    """ Tests sum_of_digits for cases:
        11111
    """
    result = sum_of_digits(11111)
    assert 5 == result, "11111 does not return 5, it returns " + str(result)


def __test_sum_digits_of_non_negatives():
    """ Tests sum_digits_of_non_negatives for cases:
         [1, 12, 73, 999, 0]
    """
    result = sum_digits_of_non_negatives([1, 12, 73, 999, 0])
    assert [1, 3, 10, 27, 0] == result, "[1, 12, 73, 999, 0] does not return [1, 3, 10, 27, 0], it returns " + str(result)


def __test_table_time():
    """ Tests table_time for cases:
        -7, 0, 10000 - should not throw exception or write file
        10, 30, 10 - should throw ValueError exception
    """
    filename = "erase.csv"
    if os.path.isfile(filename):  # if the file already exists, remove it.
        os.remove(filename)
    try:
        table_time(filename, -7, 0, 10000)
    except ValueError: 
        assert False, "threshold <= 2 throws an exception"
    else:
        assert not os.path.isfile(filename), "file created when length >= threshold"

#     try:
#         table_time("should_not_write.csv", 10, 30, 10)
#     except ValueError as e: 
#         if len(e.args) > 0 and e.args[0].startswith('empty range for randrange()'):
#             raise e # not the ValueError I raised
#     else:
#          assert False, "30 - 10 as lower - upper does not throw an exception"


if __name__ == '__main__':
    __test_sum_of_digits()
    __test_sum_digits_of_non_negatives()
    __test_table_time()
    table_time("output_always_sum.csv", 900000, 10000000, 1000000000)
    table_time("output_never_sum.csv", 900000, -7, -1)
    table_time("output_sometimes_sum.csv", 900000,-100000, 1000000)
