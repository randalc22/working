class reg:
    def __init__(self,name,age,country):
        self.name=name
        self.age=2020-age
        self.country=country
    
    def regfunct(self, input):
        print("{} {} {} {}".format(input, self.name, self.age, self.country))

for i in range (1,5):
    x=input('Enter name: ')
    y=int(input('Enter DOB:'))
    z=input('Enter country:')

    mark="mark"+str(i)
    print(type(mark))
    
    mark=reg(x,y,z)
    print(type(mark))
  
    mark.regfunct("test")
    
print("is this working?")

print("Test additional text")