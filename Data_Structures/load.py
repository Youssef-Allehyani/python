def load_numbers(file_name):
    numbers = list()
    with open(file_name) as n:
        for line in n :
            numbers.append(int(line))
    return numbers        
     
     
