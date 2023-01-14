class Sample:
#this is a constructor.
    def _init_(self):
        self.x = 10
    #this is an instance method.
    def modify(self):
        self.x+=1
    #create 2 instances
s1 = Sample()
s2 = Sample()
print( s1.x)
print( s2.x)
    #modify x in s1
s1.modify()
s2.modify()
print(s1.x)
print( s2.x)
for i in range(9):
    s1.modify()
print(s1.x)
