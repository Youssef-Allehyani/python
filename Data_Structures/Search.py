from List import List
class Search :
#--------------------//Liner search//----------------------------- 
   def linear_search(List,value):
    #Return index if found the value otherwise return none
    for i in range(0,len(List)):
        if List[i] == value :
            return i
    return None

#--------------------//binary search//----------------------------- 
   def binary_search(List , value):
        Minimum = 0
        Maximum = len(List) - 1
        
        while  Minimum <= Maximum :
            midpoint = (Maximum + Minimum)// 2 
            if List[midpoint] == value :
                return midpoint
            elif value > List[midpoint]:
                Minimum = midpoint +1 
            else:
                Maximum = midpoint - 1
        return None
   def recursive_binary_search(List , value): 
      
       if len(List) == 0 :
           return False
       else:
           midpoint = len(List)//2
       
       if  List[midpoint] == value: 
           return midpoint
       else:
           if List [midpoint] >= value:
              return Search.recursive_binary_search(List[:midpoint],value)
           else:
              return Search.recursive_binary_search(List[midpoint+1:],value)          
                          
    

    

   





# ---------------// print the resulte // -------------------------   
   def verify(index):
    if index is not None:
        print (f"the index if value is {index}")
    else:
        print ("your value is not existe ")


