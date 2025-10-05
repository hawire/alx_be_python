class SimpleCalculator:
    def add(self, a, b):
        self.a = a
        self.b = b
        return a + b
    
    
    def subtract(self, a, b):
        self.a = a
        self.b = b
        return a - b
    
    def multiply(self, a, b):
        self.a = a
        self.b = b
        return a * b
    
    def divide(self, a, b):
        self.a = a
        self.b = b
        if b == 0:
            return None
        return a / b
