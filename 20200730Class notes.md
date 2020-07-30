# 20200727ClassNotes.md
```
Person.py
In employee.py you might have a problem that says Person not defined
Well there are two easy ways to fix this

The first solution is instead of import person do:
from person import Person in line 1

Another way is to do
person.Person instead of just Person in line 3

To define people you need this line:

def __repr__(self):
        return "person:"+self.name +"("+ self.ssn+")"+str(self.age)

And you can change the person to whatever you want like employee, manager, student, teacher etc.

You also need this line:

p = Person("John", "111-33-2222", "Male",  13)
print(p)

Let me explain

The p is a variable
You can make the variable anything you want because it's just a variable
The Person is the whole code
The ("John", "111-33-2222", "Male",  13) is the name, social security number, gender, and age
You write this information because of this line:
def __init__(self, name, ssn, gender, age):
The last line means to print this line:
("John", "111-33-2222", "Male",  13)
This is because the p basically owns that line
So the output of person.py is:

person:Grace(111-33-2222)13
person:June(111-22-3333)21
student:Jennifer(444-732-9999)30
student:Robert(444-732-9999)30
teacher:John(444-732-9999)30

Another thing you can do is make the people say things 
For example, you can make the teacher say "i'm grading the papers" with only 2 lines.

This is the first line:

def gradePapers(self):
        print(self.name+": I'm grading the papers")

Def means that it defines gradePapers
it doesn't actually do anythin until you pull it out and actually use it
The second line is where you can input anything for anyone to say
For example, I can change I'm grading the papers to I'm teaching the class if I wanted to
The self.name+ means that you want to write I'm grading the papers next to the teacher's name

The second line is

t1.gradePapers()

This line calls the defined line 
without this line, the def line would do absolutely nothing

Here is the teacher's profile:

t1 = Teacher("John", "444-732-9999", "Male",  30)
print(t1)

As you can see, the teacher is t1
That is why you need t1 in front of gradePapers

I did this to a few more people
This is the code:

class Person:
    def __init__(self, name, ssn, gender, age):
        self.name = name
        self.ssn = ssn
        self.gender = gender
        self.age = age
    def __repr__(self):
        return "person:"+self.name +"("+ self.ssn+")"+str(self.age)
class Student(Person):
    def __repr__(self):
        return "student:"+self.name +"("+ self.ssn+")"+str(self.age)

    def doHomework(self):
        print(self.name+": I'm doing the homework")

class Teacher(Person):
    def __repr__(self):
        return "teacher:"+self.name +"("+ self.ssn+")"+str(self.age)
    
    def gradePapers(self):
        print(self.name+": I'm grading the papers")

p = Person("Grace", "111-33-2222", "Male",  13)
print(p)
p1 = Person("June","111-22-3333","Female",  21)
print(p1)
s1 = Student("Jennifer", "444-732-9999", "Male",  30)
print(s1)
s2 = Student("Robert", "444-732-9999", "Male",  30)
print(s2)
t1 = Teacher("John", "444-732-9999", "Male",  30)
print(t1)
s1.doHomework()
s2.doHomework()
t1.gradePapers()

And here is the outcome:

person:Grace(111-33-2222)13
person:June(111-22-3333)21
student:Jennifer(444-732-9999)30
student:Robert(444-732-9999)30
teacher:John(444-732-9999)30
Jennifer: I'm doing the homework
Robert: I'm doing the homework
John: I'm grading the papers

In Employee
In employee.py you might have a problem that says Person not defined
Well there are two easy ways to fix this

The first solution is instead of import person do:
from person import Person in line 1
```
```
In Employee.py you might have a problem that says Person not defined
Well there are two easy ways to fix this

The first solution is instead of import person do:
from person import Person in line 1
Another way is to do
person.Person instead of just Person in line 3

Employee.py is a little different than Person.py

Instead of making the employees say things, they have ID numbers
The first part of Employee.py is the same as Person.py
Like it still has name, ssn, gender, and age
But instead of this:


    def doHomework(self):
        print(self.name+": I'm doing the homework")

It has this:

employeeID = ""

And this:

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

This kind of has the same concept as the teacher
It's just instead of printing something, it's an ID

There is also this line that calls the def:

m1.setEmployeeID("728-01")
print(m1.employeeID)

It just tells the code what ID to print and it prints it

I added two people to the code

Here is the code:

from person import Person

class Employee(Person):
    employeeID = ""
    def __repr__(self):
        return "employee:"+self.name +"("+ self.ssn+")"+str(self.age)
    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID
class Manager(Employee):
    def __repr__(self):
        return "manager:"+self.name +"("+ self.ssn+")"+str(self.age)
e1 = Employee("Yichen","050-32-2999","Female",24)
print(e1)

m1 = Manager("Yichen","050-32-2999","Female",24)
print(m1)
e1.setEmployeeID("728-00")
print(e1.employeeID)
m1.setEmployeeID("728-01")
print(m1.employeeID)


And here is the outcome:


person:Grace(111-33-2222)13
person:June(111-22-3333)21
student:Jennifer(444-732-9999)30
student:Robert(444-732-9999)30
teacher:John(444-732-9999)30
Jennifer: I'm doing the homework
Robert: I'm doing the homework
John: I'm grading the papers
employee:Yichen(050-32-2999)24
manager:Yichen(050-32-2999)24
728-00
728-01

That's all!





```