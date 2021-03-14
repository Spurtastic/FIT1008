from tester import swap


class SelectionSort:

    def __init__(self):
        self.array = []

    def sort(self, array):
        print("hello")
        self.array+=array
        array_length = len(self.array)
        print(array_length)
        for i in range(array_length):
            min_index = i 
            for j in range(min_index+1, array_length):
                if self.array[min_index]>self.array[j]:
                    min_index = j     
            swap(self.array,i,min_index)
        return self.array

    def swap(self, array, i, j ):
        self.array[i],self.array[j]= self.array[j],self.array[i]


def duplicate(a_list):
    hash = dict()

    for i in a_list:
        try:
            hash[i]+=1
        except KeyError:
            hash[i]=1
    print(len(hash))
    for x in hash.keys():
        if hash[x]>=2:
            print(None)
        elif isinstance(x, str):
            




a_list = [1,2,1,1,2,3,4,5,6,7]

duplicate(a_list)

