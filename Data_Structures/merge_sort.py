from linked_list import Linked_list
import sys
import random
from load import load_numbers
class Sort:
#-------------------//merge sort for list\\--------------------------------
    def merge_sort(List):

        if len(List) <= 1:
            return List


        left_half,right_half = Sort.split(List)

        left = Sort.merge_sort(left_half)
        right = Sort.merge_sort(right_half)
    
        return Sort.merge(left,right)
    def split(List):




        mid = len(List) //2
    
        left = List[:mid]
        right = List[mid:]

        return left,right

    
        while not is_sorted(values):
            random.shuffle(values)
            
        return values 
    def merge(left,right):

        new_list = []
        i=0
        j=0
    

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append( left[i])
                i+=1
            else:
                new_list.append(right[j])
                j+=1
        while i < len(left):
            new_list.append(left[i])
            i+=1
        while j < len(right):
            new_list.append(right[j])
            j+=1
        return new_list                   
    def verify_sort(List):
        if len(List) <= 1:
            return True
        return List[0] <= List[1] and  Sort.verify_sort(List[1:])
# ----------------// improve merge sort \\-----------------------------
    def improve_merge_sort(List):
        if len(List) <= 1 :
            return List
        mid_point = len(List)//2    
        left_half = Sort.improve_merge_sort(List[:mid_point])
        right_half = Sort.improve_merge_sort(List[mid_point:])   
        sorted_list = list()
        index_left = 0
        index_right = 0 
        while index_left < len(left_half) and index_right < len(right_half):
            if left_half[index_left] < right_half[index_right]:
              
                sorted_list.append(left_half[index_left])
                index_left +=1
            else:
             
                sorted_list.append(right_half[index_right])
                index_right +=1
        sorted_list += left_half[index_left:]
        sorted_list+= right_half[index_right:]
        return sorted_list        

#------------------// bogo sort \\-------------------------------------
    def is_sorted(values):
        for index in range(len(values)-1):
            if values[index] > values[index+1]:
                return False
        return True   
    def bogo_sort(values):
        while not Sort.is_sorted(values):

            random.shuffle(values)
        return values 
#-----------------//selection sort\\--------------------------------------  
    def selection_sort(listed):
        sort_list =[]
        for i in range(0,len(listed)) :
            index_to_move = Sort.index_of_min(listed)
            sort_list.append(listed.pop(index_to_move))
        return sort_list
    def index_of_min(listed):
        Minemum = 0
        for n in range(1,len(listed)):
            if listed[n] < listed[Minemum]:
                Minemum = n
        return Minemum
# ---------------//quick sort \\--------------------------------------------
    def quick_sort(numbers):
        if len(numbers) <=1:
   
            return numbers
        less_privot = []
        greateer_then_privot = []    
        privot = numbers[0]

        
        for value in numbers[1:]:
            if value <= privot:
                less_privot.append(value)
            else:
                greateer_then_privot.append(value)

        return Sort.quick_sort(less_privot) + [privot] + Sort.quick_sort(greateer_then_privot) 




class Linked_list_sortition:
    def sort_linked_list(linked_list):
        if   linked_list.size() == 1 :
            return linked_list
        elif linked_list.head is None:
            return linked_list   
           

        left_half , right_half = Linked_list_sortition.split(linked_list)
        

        left = Linked_list_sortition.sort_linked_list(left_half)       
        right = Linked_list_sortition.sort_linked_list(right_half)

        return Linked_list_sortition.merge(left,right)

    def split(linked_list):
        if  linked_list == None or linked_list.head == None:
            left_half = linked_list
            right_half = None
            return left_half,right_half
        else:
            size = linked_list.size()
            mid = size // 2
            mid_node = linked_list.node_at_index(mid-1)
            left_half = linked_list
            right_half = Linked_list()
            right_half.head = mid_node.next_Node
            
            mid_node.next_Node = None    

        return left_half,right_half
    def merge(left,right):

        merge = Linked_list()
        merge.add(0)
        
        
        current = merge.head
        
    

        left_head = left.head
        
        right_head = right.head
      

        while left_head or right_head:
            

            if left_head is None:
                current.next_Node = right_head
                
                right_head = right_head.next_Node
                

            elif right_head is None:
                current.next_Node = left_head
                left_head = left_head.next_Node
            else:
                

                left_data = left_head.data    
                right_data = right_head.data 

                if left_data < right_data :
                    current.next_Node = left_head
                    left_head = left_head.next_Node
                else:
                    current.next_Node = right_head
                    right_head = right_head.next_Node
                   
            current = current.next_Node
            
        head = merge.head.next_Node    
        merge.head = head
        return merge




# alist = [59,80,34,2,32,56,32,53]

# print(Sort.imrove_merge_sort(alist))













