# solver.py
from linear_equation import LinearEquation
from quadratic_equation import QuadraticEquation

class EquationSolver:
    """Main class that handles user interaction and solves equations"""
    def __init__(self):
        self.equations = []
    
    def get_equation_type(self):
        """Get the type of equation to solve from the user"""
        while True:
            print("\nEquation Solver")
            print("1. Linear Equation (ax + b = c)")
            print("2. Quadratic Equation (ax² + bx + c = 0)")
            print("3. Exit")
            
            choice = input("\nSelect equation type (1-3): ")
            
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
    
    def get_linear_equation_input(self):
        """Get linear equation coefficients from user"""
        print("\nEnter the coefficients for the linear equation: ax + b = c")
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter constant c: "))
            return a, b, c
        except ValueError:
            print("Error: Please enter valid numbers.")
            return None
    
    def get_quadratic_equation_input(self):
        """Get quadratic equation coefficients from user"""
        print("\nEnter the coefficients for the quadratic equation: ax² + bx + c = 0")
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            return a, b, c
        except ValueError:
            print("Error: Please enter valid numbers.")
            return None
    
    def run(self):
        """Main method to run the equation solver"""
        while True:
            choice = self.get_equation_type()
            
            if choice == "1":  # Linear Equation
                coefficients = self.get_linear_equation_input()
                if coefficients:
                    a, b, c = coefficients
                    equation = LinearEquation(a, b, c)
                    equation.solve()
                    equation.display_solution()
                    equation.save_to_file()
                    self.equations.append(equation)
            
            elif choice == "2":  # Quadratic Equation
                coefficients = self.get_quadratic_equation_input()
                if coefficients:
                    a, b, c = coefficients
                    equation = QuadraticEquation(a, b, c)
                    equation.solve()
                    equation.display_solution()
                    equation.save_to_file()
                    self.equations.append(equation)
            
            elif choice == "3":  # Exit
                print("\nThank you for using the Equation Solver. Goodbye!")
                break
            
            input("\nPress Enter to continue...")
