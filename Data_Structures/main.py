from List import List
from Search import Search
import time
from merge_sort import Sort, Linked_list_sortition
from linked_list import Linked_list
# --------------//Print the list \\-------------------------------
list1 = List.full_List()
print("The list is:",list1)
# ---------------------//Tist linear search \\-------------------------
print("----------using linear search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.linear_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")
# -----------------------// this binary ssearch \\ --------------------
print("----------using binary search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.binary_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")
# -----------------------// this recursive binary search \\ --------------------
print("----------using recursive binary search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.recursive_binary_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")

#--------------------// chack if the List is sorted or not \\--------------------
print("--------// chack if the List is sorted or not \\\\-------")
alist = [59,80,34,2,32,56,32,53]
print(alist)
print(Sort.verify_sort(alist))
sorted_list=Sort.merge_sort(alist)
print(sorted_list)
print(Sort.verify_sort(sorted_list))

#------------------// sort lkinked list \\------------------------------------- 
print("--------// sort lkinked list \\\\-------")

l = Linked_list()
l.add(20)
l.add(30)
l.add(10)
l.add(5)
l.add(25)
l.add(40)

print(l)

sorted_link_list = Linked_list_sortition.sort_linked_list(l)
print ( sorted_link_list)

