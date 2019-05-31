
class Classroom:
    
    classroom_list=['6a','6b','6c','6d','7a','7b']
    
        
    @staticmethod
    def search_classroom(class_room):
        Classroom.class_room=class_room.upper()
        if Classroom.class_room in Classroom.classroom_list:
            return("found")
        else:
            return(-1)
   
class_obj=Classroom()
class_room="7a"
if (class_obj.search_classroom(class_room)!= -1):
    print("class_room found")
else:
    print("class_room not found")
