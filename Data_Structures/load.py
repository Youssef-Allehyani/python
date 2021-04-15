import sys
# from merge_sort import Sort
def load_numbers(file_name):
    numbers = list()
    with open(file_name) as n:
        for line in n :
            numbers.append(int(line))
    return numbers        
def load_strings(file_name):
  strings = []
  with open(file_name) as f:
    for line in f:
      strings.append(line.rstrip())
  return strings
     

                
# name = load_strings(sys.argv[1])
# sorted_names = Sort.quick_sort(name)

# for n in sorted_names:
#     print(n)


# search_names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", "Guy Lashbaugh", 
# "Ginger Schlossman", "Suellen Luaces", "Jamey Kirchgesler", "Amiee Elwer", "Lacresha Peet",
# "Leonia Goretti", "Carina Bunge", "Renee Brendeland", "Andrew Mcgibney", "Gina Degon", 
# "Deandra Pihl", "Desmond Steindorf", "Magda Growney", "Tawana Srivastava", "Tammi Todman", 
# "Harley Mussell", "Iola Bordenet", "Edwardo Khela", "Myles Deanne", "Elden Dohrman", 
# "Ira Hooghkirk", "Eileen Stigers", "Mariann Melena", "Maryrose Badura", "Ardelia Koffler", 
# "Lacresha Kempker", "Charlyn Singley", "Lekisha Tawney", "Christena Botras", "Mike Blanchet", 
# "Cathryn Hinkson", "Errol Shinkle", "Mavis Bhardwaj", "Sung Filipi", "Keiko Dedeke", 
# "Lorelei Morrical", "Jimmie Lessin", "Adrianne Hercules", "Latrisha Haen", "Denny Friedeck",
# "Emmett Whitesell", "Sina Sauby", "Melony Engwer", "Alina Reichel", "Rosamond Shawe", 
# "Elinore Benyard", "Sang Bouy", "Ed Aparo", "Sheri Wedding", "Sang Snellgrove",
# "Shaquana Sones", "Elvia Motamed", "Candice Lucey", "Sibyl Froeschle", 
# "Ray Spratling", "Cody Mandeville", "Donita Cheatham", "Darren Later",
# "Johnnie Stivanson", "Enola Kohli", "Leann Muccia", "Carey Philps", 
# "Suellen Tohonnie", "Evelynn Delucia", "Luz Kliment", "Lettie Jirjis", "Francene Klebe",
# "Margart Scholz", "Sarah Growden", "Glennis Gines", "Rachael Ojima", "Teofila Stample",
# "Narcisa Shanley", "Gene Lesnick", "Malena Applebaum", "Norma Tingey", 
# "Marianela Mcmullen", "Rosalva Dosreis", "Dallas Heinzmann", "Sade Streitnatter", "Lea Pelzel",
# "Judith Zwahlen", "Hope Vacarro", "Annette Ayudan", "Irvin Cyree", "Scottie Levenstein", 
# "Agustina Kobel", "Kira Moala", "Fawn Englar", "Jamal Gillians", "Karen Lauterborn", 
# "Kit Karratti", "Steven Deras", "Mary Rosenberger", "Alonso Viviano"]

# # Now let's implement the search function. Compared to the sorting 
# def index_of_item(List,item):
#     for i in range(0,len(List)):
#         if item == List[i]:
#             return i
#     return None
# for n in search_names:
#     index = index_of_item(name,n)
#     print(index) 
# 

   
     
     
