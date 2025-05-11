# linear_equation.py
from equation import Equation

class LinearEquation(Equation):
    """Class for solving linear equations of the form ax + b = c"""
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.equation_type = "Linear"
        self.equation_string = f"{a}x + {b} = {c}"
    
    def solve(self):
        """Solve the linear equation"""
        # Check if the equation is solvable
        if self.a == 0:
            self.solution = f"Equation: {self.equation_string}\nUnsolvable equation: coefficient of x is zero."
            return
        
        # Calculate the solution
        x = (self.c - self.b) / self.a
        self.solution = f"Equation: {self.equation_string}\nSolution: x = {x}"
        return x
