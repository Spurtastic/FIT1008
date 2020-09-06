def replacelateWithXtime(the_list,replacewith,Xtime):
    # the outer loop runs O(n) times
    for i in range(len(the_list)):
        later = i+1
        replaced = 0
    # here the loop length irregardless of the previous one will always be the length of the list it self, so this will also be O(n)   
        if not the_list[i] == replacewith:
            while (replaced < Xtime) and (later < len(the_list)):
                if the_list[later] == the_list[i]:
                    the_list[later] = replacewith
                    replaced += 1
                later += 1


print(replacelateWithXtime([1,3,3,6,6,1,1,2,2,4,4], 5, 2))