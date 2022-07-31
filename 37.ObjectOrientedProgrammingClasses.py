"""
class car():
    model="Renault Megane"
    colour="White"                  #when we write this features, these features doesn't be special any object
    horsepower=110                  #these features don't special to object, they are speacial to class
    cylinder=4

car1=car()  #I know that there is the experiences in car1 

print(car1)   #it is saying -main- car, we created the object from car class

car2=car()

print(car1.model)
print(car2.horsepower)
print(car2.model)

print(car.model)   #I can make this too

#If we want to product an object with different values what will we do
#we will use init function

print(dir(car1))  #That I understood if we don't describe the default functions 
                  #python describes otomatically

                    #if we describe, we are saying to python, don't describe, I will decribe.

#init function is constructor function .
#this function is first called function, while we create our object. 
#if we give any value to this function, our object carries various features
#we don't need to call this function as special.
#this function called otomatically while we create the objects.

class car10():
    model="Renault Megane"
    colour="White"                  
    horsepower=110                  
    cylinder=4
    def __init__(self):
        print("init function was called")

car3=car10()    #init function was called otomatically
"""


class car():
    def __init__(self,model,colour,horsepower,cylinder):
        self.model=model
        self.colour=colour
        self.horsepower=horsepower
        self.cylinder=cylinder

car1=car("Renault Megane","Silver",110,4)

print(car1.model)














    