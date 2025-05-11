# equation.py
import os

class Equation:
    """Base class for equations"""
    def __init__(self):
        self.solution = None
        self.equation_type = None
    
    def solve(self):
        """To be implemented by subclasses"""
        pass
    
    def display_solution(self):
        """Display the solution to the console"""
        print(f"\n{self.equation_type} Equation Solution:")
        print(self.solution)
    
    def save_to_file(self, filename="equation_solutions.txt"):
        """Save the solution to a text file"""
        # Create the solutions directory if it doesn't exist
        if not os.path.exists("solutions"):
            os.makedirs("solutions")
        
        filepath = os.path.join("solutions", filename)
        
        # Write the solution to the file, appending if the file exists
        with open(filepath, "a") as file:
            file.write(f"-----------------------------------\n")
            file.write(f"Equation Type: {self.equation_type}\n")
            file.write(f"{self.solution}\n")
            file.write(f"-----------------------------------\n\n")
        
        print(f"\nSolution saved to {filepath}")
