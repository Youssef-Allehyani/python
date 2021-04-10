import random
from merge_sort import Sort
class List:
    def full_List():
        RandomList = [random.randint(1,100) for i in range(10)]
        unduplicate_List = []
        [unduplicate_List.append(x) for x in RandomList if x not in unduplicate_List]
        
        return  Sort.merge_sort(unduplicate_List) 


def random_number_files():
    for i in range(100):
        numbers= open("Data_Structures/Files/100numbers.txt","a") 
        random_number = str(random.randint(1,10000))
        numbers.write(f"\n{random.randint(1,10000)}")
    numbers.close()        
# random_number_files()        


