class Student:
    no_of_student = 0
  
    def __init__(self, name , id_number , age= 18 , courses="none" , Email= "university@st.mmiu.com"):
        self.__name = name 
        self.__age =age 
        self.__courses = courses
        self.__Email = Email
        self.__id_number = id_number
        Student.no_of_student += 1
    def dsccribe(self):
        print(f"name is {self.__name}, id number is {self.__id_number}, age is {self.__age} , courses {self.__courses} , E-mail {self.__Email}")
#----------------------------------------------------------------------------------------------------------------------------        
    def get_name(self):
        return  self.__name 
    def set_name(self ,new_name):
        self.__name = new_name
#----------------------------------------------------------------------------------------------------------------------------        
    def get_age(self):
        return self.__age 
    def set_age(self ,new_age):
        self.__age = new_age    
#------------------------------------------------------------------------------------------------------------------------------
    def get_id_number(self):
        return self.id_number    
#------------------------------------------------------------------------------------------------------------------------------     
    def get_courses(self):
        self.__courses
    def set_addCourses(self, add_new_cours):
        if len(self.__courses) < 4 :
            self.__courses.append(add_new_cours)
        else:
            print("you have Maximum courses")  
    def set_deletCourses(self, delet_cours):
        if len(self.__courses) > 2 :
            self.__courses.remove(delet_cours)
        else:
            print("you have Minemum courses")          
#------------------------------------------------------------------------------------------------------------------------------
    def get_Email(self):
        self.__Email            


student1 =Student("youssef", 439009898 ,21,["Algorithm ","it","shariah","science"],"youssef@st.mmiu.com")
student2 =Student ("mohammad",441998787,19,["shariah","Quran","parallel computer"],"mohammad@st.mmiu.com")
student3 =Student ("nouh",438998989,22,["shariah","it","math"],"nouh@st.mmiu.com")

student1.set_name("Youssef")
student2.set_name("Mohammed")
student3.set_name("Nouh")

student1.set_addCourses("Quran")
student2.set_deletCourses("Quran")
student3.set_age(23)

student1.dsccribe()
student2.dsccribe()
student3.dsccribe()