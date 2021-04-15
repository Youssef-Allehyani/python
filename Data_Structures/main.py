import time
from List import List
from Search import Search
from merge_sort import Sort, Linked_list_sortition
from linked_list import Linked_list
from load import load_numbers, load_strings
# --------------the list-------------------------
alist = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1] 
# load_numbers("Data_Structures/Files/1000numbers.txt")
# --------------//Print the list \\-------------------------------
list1 = List.full_List()
print("The list is:",list1)
# ---------------------//Tist linear search \\-------------------------
print("\n----------using linear search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.linear_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")
# -----------------------// this binary ssearch \\ --------------------
print("\n----------using binary search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.binary_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")
# -----------------------// this recursive binary search \\ --------------------
print("\n----------using recursive binary search ----------")
StartTime = time.perf_counter_ns()
resulte = Search.recursive_binary_search(list1,98)
lastTime = time.perf_counter_ns()
Search.verify(resulte)
print(f"time of monitor: {(lastTime-StartTime)}")

#--------------------// chack if the List is sorted or not  \\--------------------
print("\n--------// chack if the List is sorted or not \\\\-------")
# print(alist)
# print(Sort.verify_sort(alist))
StartTime = time.perf_counter_ns()
sorted_list=Sort.merge_sort(alist)
EndTime = time.perf_counter_ns()
print(f"sorted_list {sorted_list} \ntime of monitor: {(EndTime-StartTime)}ns ")
# print(Sort.verify_sort(sorted_list))

#------------------// sort lkinked list \\------------------------------------- 
print("\n--------// sort lkinked list \\\\-------")
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

#------------------// bogo sort \\------------------------------------- 
print("\n-----------//bogo sort \\\\ ----------------")
alist1= load_numbers("Data_Structures/Files/numers.txt")
StartTime = time.perf_counter_ns()
sorted_bogo = Sort.bogo_sort(alist1)
EndTime = time.perf_counter_ns()
print(f"sort_list:{sorted_bogo} \ntime of monitor: {(EndTime-StartTime)} ")
#------------------// selection sort \\-------------------------------------- 
print("\n-----------// selection sort \\\\ ----------------")
StartTime = time.perf_counter_ns()
sorted_selection = Sort.selection_sort(alist)
EndTime = time.perf_counter_ns()
print(f"sort_list:{sorted_selection} \ntime of monitor: {(EndTime-StartTime)} ")

#-----------------// quick sort \\--------------------------------------------
print("\n----------// quick sort\\\\------------------------ ")
StartTime = time.perf_counter_ns()
sorted_list = Sort.quick_sort(alist)
EndTime = time.perf_counter_ns()
print(f"sort_list:{sorted_selection} \ntime of monitor: {(EndTime-StartTime)} ns ")