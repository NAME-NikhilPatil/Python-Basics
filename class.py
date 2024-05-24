class Greeter(object): 
    def __init__(self, name): 
        self.name = name
    def greet(self, loud=False): 
        if loud: 
            print('Hello, %s!' % self.name.upper()) 
        else: 
            print('Hello, %s' % self.name) 

g = Greeter('Good Morning Nikhil') 
g.greet() 
g.greet(loud=True)
