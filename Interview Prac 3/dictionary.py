from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit


class Statistics:
    """Class contains the ability to load the data collected from running dictionary as well as loading the statistical data"""

    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time) -> tuple:
        """

        :param hash_base:
        :param table_size:
        :param filename:
        :param max_time:
        :return:
        """

        # the hash table is first initialised
        init_table = Dictionary(hash_base, table_size)

        try:
            start_time = timeit.default_timer()
            words = init_table.load_dictionary(filename, max_time)
            time = (timeit.default_timer() - start_time)
            (collision_count, probe_total, probe_max, rehash_count) = init_table.hash_table.statistics()
            return words, collision_count, probe_total, probe_max, rehash_count, time

        # basically when the function cant read all the lines within the stipulated time, the stated time is assigned
        except TimeoutError:

            # uses the ability to call the Class Dictionary's variable call to count the total lines in the file
            words = init_table.count
            time = max_time
            (collision_count, probe_total, probe_max, rehash_count) = init_table.hash_table.statistics()
            return words, collision_count, probe_total, probe_max, rehash_count, time

    def table_load_statistics(self, max_time: int) -> None:
        b = [1, 27183, 25026]
        table_size = [ 25027, 40221, 1000081]
        filename = ["english_large.txt", "english_small.txt", "french.txt"]
        combos = [(base, t, f) for base in b for t in table_size for f in filename]
        file = open("output_task2.csv", "w")
        file.write('Name'+','+'Table Size'+','+'Base'+','+'Number of Words'+','+'Collision Count'+','+'Probe_total'+','+'Probe_max'+','+'Rehash Count'+','+'Time Taken'+"\n")
        for base ,t ,f in combos:
            stats = self.load_statistics(self, base, t, f, max_time)
                    # Name   tblesize   base           words            collision count    probe total       rehash count      time taken       time taken
            file.write(f+","+str(t)+","+str(base)+","+str(stats[0])+","+str(stats[1])+","+str(stats[2])+","+str(stats[3])+","+str(stats[4])+","+str(stats[5])+"\n")
        file.close()

class Dictionary:
    # returns None
    def __init__(self, hash_base: int, table_size: int):
        self.hash_base = hash_base
        self.table_size = table_size
        self.hash_table = LinearProbeHashTable(self.hash_base, self.table_size)

    # returns integer
    def load_dictionary(self, filename: str, time_limit: int = None):
        self.count = 0

        # if the time is not None then start the timer
        if time_limit!=None:
            timer_start = timeit.default_timer()
            with open(filename, 'r', encoding= 'UTF-8') as file:
                for item in file:
                    self.add_word(item.rstrip("\n").lower())
                    timer_end = (timeit.default_timer() - timer_start)
                    self.count += 1
                    # print(self.count)
                    if timer_end > time_limit:
                        raise TimeoutError

        else:
            with open(filename, 'r', encoding='UTF-8') as file:
                for item in file:
                    self.add_word(item.rstrip("\n").lower())
                    self.count+=1
        file.close()
        return self.count
        
                
    # returns None
    def add_word(self, word: str):
        self.hash_table.insert(word.lower(),1)

    #returns bool
    def find_word(self, word: str):
        if word.lower() in self.hash_table:
            return True
        return False

    #returns None
    def delete_word(self, word: str):
        del self.hash_table[word.lower()]

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
                res = str(input("File Name? \n"))
                self.load_dictionary(res)
                print(f"{res} is now loaded")
            
            elif input_recieved == 2:
                res = str(input("Which word would you like to delete? \n"))
                self.delete_word(res)
                if self.find_word(res):
                    print(f"{res} is now deleted from the Hash")
                else:
                    print(f"{res} is not in the Hash try inputting it into the hash")


            elif input_recieved == 3:
                res = str(input("Which word are you looking for? \n"))
                if self.find_word(res):
                    print(f"{res} is in the Dictionary")

                else:
                    print(f"{res} is not in the Dictionary")

            elif input_recieved == 4:
                res = str(input("Word to add? \n"))
                self.add_word(res)
                print(f"{res} is added to the dictionary")
                
            else:
                res="invalid input try again"
                print(res)



    # TODO


if __name__ == '__main__':
    # TODO
    # dict = Dictionary(31, 250727)
    # (dict.load_dictionary("english_large.txt",10))
    # print(dict.count)
    # stat = Statistics.load_statistics(Statistics, 31, 250727, "french.txt", 1)
    # print(stat)
    stat = Statistics.table_load_statistics(Statistics, 10)
    print(stat)





