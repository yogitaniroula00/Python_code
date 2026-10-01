# 
""" """
name="yogita"
name= input("enter the name")
age= int(input("enter the age"))
location= input("enter the location")
# concate
print("My name is "+name+" age is" +str(age) + "i live in" + location)
#f string
print(f"My name is {name} age is {age} and the location is {location}")
#  format old version
print("My name is %s and age is %d and location is %s" %(name,age,location))
# format new version
print("My name is {0} and age is{1} and location is {2}".format(name,age,location))
print(type(location))