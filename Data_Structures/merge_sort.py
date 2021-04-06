class Sort:
   
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
               


