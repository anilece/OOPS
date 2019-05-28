
'''ClassName :Instructor
Attributes: instructor_name technology_skill experience avg_feedback
Methods: __init__() check_eligibility() allocate_course(technology)'''

class Instructor():
    def __init__(self):
        self.__instructor_name=None
        self.__technology_skill=None
        self.__experience=None
        self.__avg_feedback=None
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
    def set_experience(self,experience):
        self.__experience=experience
    def get_instructor_name(self):
        print(self.__instructor_name)
    def get_technology_skill(self):
        print(self.__technology_skill)
    def get_avg_feedback(self):
        print(self.__avg_feedback)
    def get_experience(self):     
        print(self.__experience)
    def check_eligibility(self):
        if self.__experience>3:
            if self.__avg_feedback>=4.5:
                return (True)
            else:
                return(False)
        else:
            if self.__avg_feedback>=4:
                return(True)
            else:
                return(False)
                
    def allocate_course(self,technology):
        if self.check_eligibility():
            if technology in self.__technology_skill:
                return(True)
            else:
                return(False)
        else:
            return(False)
ins1=Instructor()
ins1.set_instructor_name("anil")
ins1.set_experience(5)
ins1.set_avg_feedback(4.9)
skills=["Python","basic Electronics","c++"]
ins1.set_technology_skill(skills)
ins1.check_eligibility()
ins1.allocate_course("Python")
ins1.get_instructor_name()
ins1.get_experience()
ins1.get_technology_skill()
ins1.get_avg_feedback()

            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
