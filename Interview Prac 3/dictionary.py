from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit


class Statistics:

   pass

    


class Dictionary:
    # returns None
    def __init__(self, hash_base: int, table_size: int):
        self.base = hash_base
        self.table = [None] * table_size

    # returns integer
    def load_dictionary(self, filename: str, time_limit: int = None):
        
        pass

    # returns None
    def add_word(self, word: str):
        pass

    #returns None
    def find_word(self, word: str):
        pass

    #returns None
    def delete_word(self, word: str):
        pass

    #returns None
    def menu(self):
        
        usr_input = True
        while usr_input:
            print("""
            1. Read File
            2. Delete word
            3. Find Word
            4. Add Word
            5. Quit""")
            input_recieved = int(input("Input the appropriate number for your required command: "))
            if input_recieved == 5:
                usr_input = False
                res="You quit"
                return res

            elif input_recieved == 1:
                res = "File read"
                print(res)
            
            elif input_recieved == 2:
                res = "Word deleted"
                print(res)

            elif input_recieved == 3:
                res = "Word found in file"
                print(res)

            elif input_recieved == 4:
                res = "Word added"
                print(res)
                
            else:
                res="invalid input try again"
                print(res)



    # TODO


if __name__ == '__main__':
    # TODO
    dict = Dictionary(3,2)
    print(dict.menu())



