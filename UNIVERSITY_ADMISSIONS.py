'''
Class name: Student
Attributes(private)	 student_id marks age

Methods
(public)	__init__()	Create and initialize all instance variables to
validate_marks()	If data is valid, return true. Else, return false
validate_age()
check_qualification()	Validate marks and age.
'''
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_student_id(self,student_id):
        self.__student_id=student_id
    def  set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    def get_student_id(self):
        print(self.__student_id)
    def get_marks(self):
        print(self.__marks)
    def get_age(self):
        print(self.__age)
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return (True)
        else:
            return (False)
    def validate_age(self):
        if self.__age >20:
            return (True)
        else:
            return(False)
    def check_qualification(self):
        if (self.validate_age() and self.validate_marks()):
            if self.__marks>=65:
                print(self.__student_id,"is qualified")
                return True
            else:
                print(self.__student_id,"is not qualified")
                return False
            
        else:
            print(self.__student_id,"is not qualified")
            return False
                


st1=Student()
st1.set_student_id(1001)
st1.set_age(8)
st1.set_marks(90)
st1.check_qualification()
