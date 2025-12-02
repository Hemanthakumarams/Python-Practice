class Student:
    count = 0
    def __init__(self,name=None,age=None,course=None,hometown=None):
        self.Name = name
        self.Age = age
        self.__Course = course
        self.__Id = id
        self._Hometown = hometown

        if name and age and course and hometown:
            self.__regester()
            
    def get_name(self):
        return self.Name
    
    def get_age(self):
        return self.Age

    def get_course(self):
        return self.__Course
    
    def get_Id(self):
        return self.__Id
    
    def get_hometown(self):
        return self._Hometown
    
    #private method(we can call inside class only not from outside a class)
    def __regester(self):
        Student.count += 1
        self.__Id = Student.count
        return self.__Id
    
    def __update_name(self,name):
        self.Name = name

    def _update_age(self,age):
        self.Age = age