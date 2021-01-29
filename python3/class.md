defining a new class in Python.

```
class Person:
    # Class constructor
    def __init__(self, name, age):
        # Object properties
        self.name = name
        self.age = age
    
    # Method
    def say_hello(self):
        print("Hello my name is " + self.name + "!")
```
Here's how we create or instantiate an object of the class Person.
bob = Person("Bob", 32)

```
bob.name, bob.age
```

output: 
```
('Bob', 32)
```

```
bob.say_hello()
```

output: 
```
Hello my name is Bob!

```
