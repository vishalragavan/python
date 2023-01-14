class Student:
#this is a constructor.
    def _init_(self, n = '', m=0):
        self.name = n
        self.marks = m
#this is an instance method.
    def display(self):
        print('HI' , self.name)
        print('Your marks', self.marks)
#to calculate grades based on marks.
    def calculate(self):
        if(self.marks>=600):
            print('you got first grade')
        elif(self.marks>=500):
            print('second grade')
        elif(self.marks>=350):
            print('third grade')
        else:
            print('You are failed')
#create instances with some data from keyboard
n = int(input('How many students'))
i=0
while(i<n):
    name = input('ENTER NAME:')
    marks = int(input('ENTER MARKS:'))
#create Student class instance and store data
    s = Student(name, marks)
    s.display()
    s.calculate()
    i+=1
    print('+++++++++++++++++')
