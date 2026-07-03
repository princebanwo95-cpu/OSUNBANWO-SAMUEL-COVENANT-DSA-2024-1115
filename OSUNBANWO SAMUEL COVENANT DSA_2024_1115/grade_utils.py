# grade_utils.py
"""
DTS 216 Assignment - Library Module
Contains utility functions and OOP classes for grading, data structures, 
prime numbers, file processing, and matrix calculations.
"""

import numpy as np

def classify_student_grades(scores: list):
    """
    Accepts a list of 5 course scores, calculates the average, 
    and assigns a letter grade based on the syllabus scale.
    """
    if len(scores) != 5:
        raise ValueError("Exactly 5 course scores are required.")
        
    avg_score = sum(scores) / len(scores)
    
    # Grading system matching the assignment guidelines
    if avg_score >= 70:
        grade = 'A'
    elif avg_score >= 60:
        grade = 'B'
    elif avg_score >= 50:
        grade = 'C'
    elif avg_score >= 45:
        grade = 'D'
    elif avg_score >= 40:
        grade = 'E'
    else:
        grade = 'F'
        
    return {
        "individual_scores": scores,
        "average": avg_score,
        "grade": grade
    }

def demonstrate_data_structures():
    """Demonstrates basic Python data structures."""
    example_list = [10, 20, 30]                # Mutable, ordered
    example_tuple = (10, 20, 30)              # Immutable, ordered
    example_dict = {"math": 85, "english": 90} # Key-value pairs
    example_set = {10, 20, 30, 30}             # Unique elements, unordered
    
    return example_list, example_tuple, example_dict, example_set

def demonstrate_type_conversion():
    """Shows type conversion between int, float, and string."""
    num_str = "100"
    converted_int = int(num_str)
    converted_float = float(converted_int)
    back_to_str = str(converted_float)
    
    return converted_int, converted_float, back_to_str

def get_prime_numbers(limit=100):
    """Finds prime numbers between 1 and limit using loop control."""
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break  # Loop control: Stops checking if a factor is found
        else:
            primes.append(num)  # Executes if the inner loop didn't break
    return primes

def count_words_in_file(input_filename, output_filename):
    """
    Reads a text file, counts the total words, and writes the result to another file.
    Includes a try-except block to gracefully handle missing files.
    """
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        words = content.split()
        word_count = len(words)
        
        with open(output_filename, 'w') as file:
            file.write(f"The number of words in '{input_filename}' is: {word_count}\n")
        
        return f"SUCCESS: Counted {word_count} words. Result saved to '{output_filename}'."
        
    except FileNotFoundError:
        return f"EXCEPTION HANDLED: The file '{input_filename}' was not found."


class Student:
    """Base class representing a standard student profile."""
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        """Maps marks to alphabetical grades using the assignment rules."""
        if self.marks >= 70: return 'A'
        elif self.marks >= 60: return 'B'
        elif self.marks >= 50: return 'C'
        elif self.marks >= 45: return 'D'
        elif self.marks >= 40: return 'E'
        else: return 'F'


class GraduateStudent(Student):
    """Subclass inheriting from Student, extended with a research topic field."""
    def __init__(self, name, roll_number, marks, research_topic):
        super().__init__(name, roll_number, marks)
        self.research_topic = research_topic


def perform_numpy_operations():
    """
    Creates a 5x5 NumPy array with random integers between 1-100 and performs
    slicing, boolean indexing, transposing, and universal mathematical calculations.
    """
    np.random.seed(42) 
    matrix = np.random.randint(1, 101, size=(5, 5))
    
    sub_matrix = matrix[0:3, 0:3]
    filtered_values = matrix[matrix > 50]
    transposed_matrix = matrix.T
    
    square_roots = np.sqrt(matrix)
    array_mean = np.mean(matrix)
    array_std_dev = np.std(matrix)
    
    return {
        "original": matrix,
        "sliced": sub_matrix,
        "filtered": filtered_values,
        "transposed": transposed_matrix,
        "roots": square_roots,
        "mean": array_mean,
        "std_dev": array_std_dev
    }


class AcademicRecord:
    """Represents a student's academic standing based on CGPA classification rules."""
    
    def __init__(self, name, matric_number, department, level, cgpa):
        self.name = name
        self.matric_number = matric_number
        self.department = department
        self.level = level
        self.cgpa = float(cgpa)

    def calculate_class(self):
        """Classifies the student's CGPA tier according to assignment parameters."""
        if 4.50 <= self.cgpa <= 5.00:
            return "First Class"
        elif 3.50 <= self.cgpa < 4.50:
            return "Second Class Upper"
        elif 2.40 <= self.cgpa < 3.50:
            return "Second Class Lower"
        elif 1.50 <= self.cgpa < 2.40:
            return "Third Class"
        else:
            return "Pass"

    def display_information(self):
        """Prints a well-formatted breakdown of the student's record."""
        degree_class = self.calculate_class()
        print(f"Name: {self.name:<18} | Matric: {self.matric_number:<12} | "
              f"Dept: {self.department:<5} | Level: {self.level:<3} | "
              f"CGPA: {self.cgpa:.2f} -> Class: {degree_class}")
