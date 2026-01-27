class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        """
        Docstring for add
        param  :    self
        return :    a + b
        """
        return self.a + self.b
    
    def multiply(self):
        """
        Docstring for multiply
        
        param  :    self
        return :    a * b
        """
        return self.a * self.b
    
    def subtract(self):
        """
        Docstring for subtract
        
        param  :    self
        return :    a - b
        """
        return self.a - self.b
    
    def _sum_internal(self):
        """
        Docstring for _sum_internal
        
        param  :    self
        return :    a + b
        """
        return sum([self.a, self.b])
    
    def sum_squares(self):
        """
        Docstring for sum_squares
        
        param  :    self
        return :    (a + b) ** 2
        """
        x = self._sum_internal()
        return x ** 2