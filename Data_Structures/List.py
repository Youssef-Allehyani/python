import random
from merge_sort import Sort
class List:
    def full_List():
        RandomList = [random.randint(1,100) for i in range(10)]
        unduplicate_List = []
        [unduplicate_List.append(x) for x in RandomList if x not in unduplicate_List]
        
        return  Sort.merge_sort(unduplicate_List) 



