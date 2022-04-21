 ###Задача 1.  Дефинирайте клас Student, който съдържа следната информация за
#студентите: трите имена, курс, специалност, университет, електронна поща и телефонен
#номер;

class students () :
    count=0

    def __init__ ( self,name,cource,specialty,university,mail,tel.num):
        self.name=name
        self.cource=cource
        self.specialty=specialty
        self.university=university
        self.mail=mail
        self.tel.num=tel.num
    

students.count += 1
print(f'Student are createt:{ students.count}' )
    
def info_student(self):
        print( f'''The Student{self.name} in {self.cource,self.specialty}
            whith {self.mail} and {self.tel.num}''' )

student1 = students('Ivan Ivanov',1)
student2 = students('Kirril kirilov', 1)

students.info_student(student1)


