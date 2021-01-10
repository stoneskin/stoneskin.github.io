# 08 Python Objects and Classes

A class is a user-defined blueprint or prototype from which objects are created.

![class](https://cs.plu.edu/courses/cs144/spring2018/images/CookieCutter.png)

## 8.1 Create a Class and Object

See below example of Define a class, then create a Object with the class.

```python
#Define a Class
class MyClass:
    x = 5

# Create a Object with Class
p1 = MyClass()

# Use the Object
print(p1.x)
```

## 8.2 Create Object with Init

Python class could have a constrictor function for initial the class.

### 8.2.1 Create Object with initialize value

A simple Class with init function.
Notice in class, the function need pass 'self' as it first parameter.

```python
class MyClass:
 def __init__(self):
    self.name="unknow"

p1= MyClass()

print(p1.name)
```

**Note**: The `__init__()` function is called automatically every time the class is being used to create a new object.

### 8.2.2  The self Parameter

It just the name of the first parameter, and in object of class, the first paramter of method always the object itself. You could name it to any name

```python
class MyClass:
 def __init__(me):
    me.name="test"

p1= MyClass()

print(p1.name)
```

```python
class MyClass:
 def __init__(this):
    this.name="test"

p1= MyClass()

print(p1.name)
```

**Note**:
_In many other language , you don't need pass self, they use this key word to point itself._

### 8.2.3 Initial Object pass the values

Create a class to take name and value in init.

```python
class MyClass:
 def __init__(self,name,value):
    self.name = name
    self.value = value

p1= MyClass("x",100)
p2= MyClass("y",20)

print(p1.name +" = "+str(p1.value))
print(p2.name +" = "+str(p2.value))

```

## 8.3 Methods in Class

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

## 8.4 Object properties

The Properties of a object is changeable after assign.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

p1.name="Smith"
p1.age=24
p1.myfunc()
print("age="+str(p1.age)

```

**Note**
*Python is a weak type language, you always could create and modify the properties any time*

```python
p1.name="Smith"
p1.age=24
p1.myfunc()
print("age="+str(p1.age))

p1.age="twenty one"
print("age="+p1.age)
```

## 8.5 import python class from another file

Save the person class to person.py

```python
# python.py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
```

in the same folder, create a python file with below code

```python
from  person import Person

p1 = Person("John", 36)
p1.myfunc()

```

if you put your class in a sub folder /myclass/person.py
so the import will be

```python
from  myclass.person import Person

```

**Note**
your class name and directory name should avoid key works of python
<https://www.w3schools.com/python/python_ref_keywords.asp>

## 8.5 Home work

please Check you previous code, try to put them into one or more class, and each class be save in one file.
and use one main python file to import them and run the function in those classes.
