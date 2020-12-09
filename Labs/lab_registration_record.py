# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    DEGREE = ('undergraduate', 'postgraduate')
    
    def __init__(self, study_type, f_name, l_name):
        if study_type not in self.DEGREE:
            # if we raise an error we have to catch it
            raise ValueError("Not a valid option")

        self.__study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.__courses = []

    def __str__(self):
        return f"{self.student_name} {self.study_type} {self.courses}"    
    
    @property
    def study_type(self):
        return self.__study_type
    
    @study_type.setter
    def study_type(self,value):
        if value not in (self.DEGREE):
            raise ValueError
        self.__study_type = value

    @property
    def student_name(self):
        return self.__f_name, self.__l_name

    @student_name.setter
    def student_name(self, value):
        self.__f_name = value[0]
        self.__l_name = value[1]
    
    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.courses.append(value)

    @property
    def get_all_information(self):
        return self.student_name, self.study_type, self.courses

   
    

class RegistrationData:
 
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.__address = address
        self.__registration_fee = registration_fee
        try:
            self.__student_object = Student(study_type, f_name, l_name)
        except Exception as e:
            pass
        self.__s_id = s_id

 
        
    @property
    def student_object_property(self):
        return self.__student_object
    
    @property
    def student_id_property(self):
        return self.__s_id

    @student_id_property.setter
    def student_id_property(self, value):
        self.__s_id = value
    
    @property
    def address_property(self):
        return self.__address
    
    @address_property.setter
    def address_property(self, value):
        self.__address = value

    @property
    def registration_fee_property(self):
        return self.__registration_fee
    
    @registration_fee_property.setter
    def registration_fee_property(self, value):
        self.__registration_fee = value
    
    def student_information(self):
        print("Student info: ", self.student_object_property.get_all_information, self.student_id_property)
        print("Student address: ", self.address_property)
        print("Registration fee: ", self.registration_fee_property)


# r1 = RegistrationData("123 fake street", 120, "undergraduate", "Cormac", "Smith", "c19313793")
# r1.student_information()

# r1.student_id_property = "c19565656"
# r1.student_information()

# print(r1.student_object_property)



