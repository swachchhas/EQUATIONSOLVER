# utils.py
import os
from datetime import datetime

def save_solution_to_file(solution, filename="equation_solutions.txt"):
    """Helper function to save the solution to a file"""
    if not os.path.exists("solutions"):
        os.makedirs("solutions")
    
    filepath = os.path.join("solutions", filename)
    
    # Write the solution to the file, appending if the file exists
    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"-----------------------------------\n")
        file.write(f"Date and Time: {timestamp}\n")
        file.write(f"{solution}\n")
        file.write(f"-----------------------------------\n\n")
    
    print(f"\nSolution saved to {filepath}")
