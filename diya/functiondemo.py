def greet(name):
    print("first def",name)
greet("ammu")

def stud_info(name,course,rollno):
    print("Name=",name)
    print("Roll Number=",rollno)
    print("Course=",course)
stud_info(course='Mca',name='diya',rollno=42)

def greet(name,msg):
    print(name+" "+msg)
greet("ammu",'good mrng')

def greet(name,msg="how are you"):
    print(name+" "+msg)
greet("ammu",'good mrng')