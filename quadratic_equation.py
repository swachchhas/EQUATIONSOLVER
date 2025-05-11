# quadratic_equation.py
import math
from equation import Equation
from linear_equation import LinearEquation

class QuadraticEquation(Equation):
    """Class for solving quadratic equations of the form ax² + bx + c = 0"""
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.equation_type = "Quadratic"
        self.equation_string = f"{a}x² + {b}x + {c} = 0"
    
    def solve(self):
        """Solve the quadratic equation using the quadratic formula"""
        # Print the formula before solving
        print(f"Solving the equation: {self.equation_string}")
        
        if self.a == 0:
            linear_eq = LinearEquation(self.b, self.c, 0)
            x = linear_eq.solve()
            self.solution = f"Equation: {self.equation_string}\nThis is actually a linear equation.\n{linear_eq.solution}"
            return [x]
        
        # Step 1: Calculate the discriminant
        discriminant = self.b**2 - 4*self.a*self.c
        print(f"\nStep 1: Calculate the discriminant (Δ) = b² - 4ac")
        print(f"Δ = ({self.b})² - 4({self.a})({self.c}) = {self.b**2} - {4*self.a*self.c} = {discriminant}")

        result_str = f"Equation: {self.equation_string}\n"
        
        if discriminant > 0:
            # Step 2: Two real solutions
            print("\nStep 2: Two real solutions (Δ > 0)")
            x1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
            result_str += f"Two real solutions:\nx₁ = (-{self.b} + √{discriminant}) / (2 * {self.a}) = {x1}\n"
            result_str += f"x₂ = (-{self.b} - √{discriminant}) / (2 * {self.a}) = {x2}"
            solutions = [x1, x2]
        elif discriminant == 0:
            # Step 3: One real solution (repeated root)
            print("\nStep 3: One real solution (Δ = 0)")
            x = -self.b / (2*self.a)
            result_str += f"One real solution (repeated):\nx = -({self.b}) / (2 * {self.a}) = {x}"
            solutions = [x]
        else:
            # Step 4: Complex solutions (Δ < 0)
            print("\nStep 4: Two complex solutions (Δ < 0)")
            real_part = -self.b / (2*self.a)
            imag_part = math.sqrt(-discriminant) / (2*self.a)
            result_str += f"Two complex solutions:\n"
            result_str += f"x₁ = {real_part} + {imag_part}i\n"
            result_str += f"x₂ = {real_part} - {imag_part}i"
            solutions = [complex(real_part, imag_part), complex(real_part, -imag_part)]
        
        self.solution = result_str
        return solutions
