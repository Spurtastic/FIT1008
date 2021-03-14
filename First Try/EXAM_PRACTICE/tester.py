
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    

def ssort(A):
    """Here we know this is selection sort

    Args:
        A (list): has a list of integers

    Returns:
        lst: returns a sorted list after the proccess is complete
    Complexity:
        Best Case:O(n^2)
        Worst Case:O(n^2)
    Invariant:
        all the elements up till the current index i in the list will contain the smallest element. So its always true that the ints in that range is always going to be small 
    """

    for i in range(len(A)):
        min_index = i
        print(A)
        for j in range(min_index+1,len(A)):
            if A[min_index]>A[j]:
                min_index = j
        swap(A,min_index,i)
    return A


