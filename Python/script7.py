class student:
    def __init__(self,s_name,s_rollno,s_class):
        self.name = s_name;
        self.rollno = s_rollno;
        self.standard = s_class;
        print(f'{self.name} has erolled to the class {self.standard} bearing roll no {self.rollno}')

    def work(self):
        print(f'{self.name} is working on the homework')


rahul = student("Indranil Mondal",5,3);
rahul.work()