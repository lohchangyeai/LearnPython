print("Hello World!")

x = 5
y = 6
z = x*y

#this line is a sample comment
print("z=",z)

#assign single value to multiple variables
x= y= z = 100
print ("x=",x)
y+=1
print ("x=",x)
print ("y=",y)
print ("************")

#unpack a collection
fruits = ["orange", "banana", "coconut"]
x,y,z=fruits
print("The CURRENT master and UpdateText value of x=",x,"y=",y,"z=",z)
print("x="+x,"y="+y+"z=",z)

#to output number and string in the same line
x=5
y='John'
print(y,x)

#function 
def sayHello():
    local_x = 'i am local variable x'
    global global_x
    global_x = "i am Global variable x"
    print('local_x=', local_x)
    print('Hello there!')

sayHello()    
print('global_x=', global_x)


