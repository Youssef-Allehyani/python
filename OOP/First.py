class Student:
    no_of_student = 0
    def __init__(self, name , id_number , age= 18 , courses="none" , Email= "university@st.mmiu.com"):
        self.name = name 
        self.age =age 
        self.courses = courses
        self.Email = Email
        self.id_number = id_number
        Student.no_of_student += 1
    def dsccribe(self):
        print(f"name is {self.name}, id number is {self.id_number}, age is {self.age} , E-mail {self.Email}")    


student1 =Student("youssef", 439009898 ,21,["Algorithm ","it","shariah","science"],"youssef@st.mmiu.com")
student2 =Student ("mohammad",441998787,19,["shariah","Quran","parallel computer"],"mohammad@st.mmiu.com")
student3 =Student ("nouh",438998989,22,["shariah","it","math"],"nouh@st.mmiu.com")

Student.dsccribe(student1)
print(student1.age)