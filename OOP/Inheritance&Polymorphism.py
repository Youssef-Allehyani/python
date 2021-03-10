import datetime
class Person:
    def __init__(self,name,birthday):
        self.__name = name
        self.__birthday = birthday 
    def set_name(self,new_name):
        self.__name = new_name
    def get_name(self):    
        return self.__name    
    def set_birthday(self,birthday):
        self.__birthday = birthday
    def get_age(self):
        return datetime.date.today().year - self.__birthday
    def Display(self):
        return f"name is {self.__name} and age is {self.get_age()}"   


class Student(Person):
    __no_of_student = 0
    def __init__(self,name,birthday,gender,grades= {"first grade:":0}):
        super().__init__(name,birthday)
        self.__grades = grades
        self.__gender=gender
        Student.__no_of_student += 1
    def get_no_of_student(self):
        return self.no_of_student   
#------------------------------------------------------------------
    def get_grades(self):
        return self.__grades   
    def set_updategrades(self,new_grates):
        self.__grades.update({new_grates})
    def set_addnewgrade(self,naemClass,new_grate):
        self.__grades[naemClass]=new_grate
#------------------------------------------------------------------
    def get_gender(self):
        return self.__grades
#-------------------------------------------------------------------
    def Display(self):
        return super().Display()  + f" and the gender is {self.__gender} . grades are {self.__grades}"

        
        



def main():
   student1 = Student("ahmmad",2000,"male",{"math":100,"physics":80,"Quran":100})
   print(student1.Display())

if __name__ == "__main__":
    main()


        