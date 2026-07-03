# main.py
import grade_utils as gu  # Importing your custom library with an alias

print("--- QUESTION 1a: Student Grading System ---")
# 1. Provide 5 scores as required by the assignment
student_scores = [72, 65, 58, 48, 80]

# 2. Call the library function
results = gu.classify_student_grades(student_scores)

# 3. Display individual scores, average, and grade perfectly
print(f"Individual Scores : {results['individual_scores']}")
print(f"Average Score     : {results['average']:.2f}")
print(f"Assigned Grade    : {results['grade']}\n")


print("--- QUESTION 1b & 1c: Structures & Type Conversions ---")
l, t, d, s = gu.demonstrate_data_structures()
print(f"List: {l}\nTuple: {t}\nDict: {d}\nSet (duplicates removed): {s}\n")

i, f, string_val = gu.demonstrate_type_conversion()
print(f"String to Int: {i} ({type(i)})")
print(f"Int to Float: {f} ({type(f)})")
print(f"Float to String: '{string_val}' ({type(string_val)})\n")


print("--- QUESTION 1d: Prime Numbers (1-100) ---")
prime_list = gu.get_prime_numbers(100)
print(f"Prime numbers found:\n{prime_list}")

print("\n" + "="*45)
print("--- QUESTION 2: File Handling & OOP ---")
print("="*45)

# 1. Test File Handling with a non-existent file to prove your Exception Handler works
print("\n[Test 1] Testing missing file scenario:")
missing_file_test = gu.count_words_in_file("imaginary_file.txt", "output_count.txt")
print(missing_file_test)

# 2. Test File Handling with an actual file
with open("assignment_sample.txt", "w") as dummy_file:
    dummy_file.write("Python for Data Science makes parsing information incredibly straightforward.")

print("\n[Test 2] Testing valid file scenario:")
successful_file_test = gu.count_words_in_file("assignment_sample.txt", "output_count.txt")
print(successful_file_test)


# 3. Test OOP & Inheritance
print("\n[Test 3] Testing OOP Classes & Inheritance:")

# Instantiate a GraduateStudent object (which inherits capabilities from Student)
grad_student = gu.GraduateStudent(
    name="Samuel Osunbanwo", 
    roll_number="DTS-2026-001", 
    marks=82, 
    research_topic="Predictive Analytics in Data Science"
)

# Display data to verify inheritance worked beautifully
print(f"Student Name   : {grad_student.name}")
print(f"Roll Number    : {grad_student.roll_number}")
print(f"Research Field : {grad_student.research_topic}")
print(f"Score Metric   : {grad_student.marks}%")
print(f"Derived Grade  : {grad_student.calculate_grade()}") # Inherited method!

# =====================================================================
# --- QUESTION 3: NumPy Practice ---
# =====================================================================

print("\n" + "="*45)
print("--- QUESTION 3: NumPy Practice ---")
print("="*45)

# Run the NumPy operations function from your library
np_results = gu.perform_numpy_operations()

print("\n[1] Original 5x5 Random Array (1-100):")
print(np_results["original"])

print("\n[2] Sliced Matrix (Top-Left 3x3 Sub-array):")
print(np_results["sliced"])

print("\n[3] Boolean Indexing (Values > 50):")
print(np_results["filtered"])

print("\n[4] Transposed Array (Rows become Columns):")
print(np_results["transposed"])

print("\n[5] Universal Functions (ufuncs) Output:")
print(f"Mean of the Array       : {np_results['mean']:.2f}")
print(f"Standard Deviation      : {np_results['std_dev']:.2f}")
print("\nSquare Roots of individual elements (First 2 rows shown for brevity):")
print(np_results["roots"][0:2]) 

# =====================================================================
# --- QUESTIONS 4 & 5: COMPLETE THEORY & PRACTICALS ---
# =====================================================================

print("\n" + "="*50)
print("--- QUESTION 4: Theory & Loop Control ---")
print("="*50)

# --- 4(a) type() Function Explanations ---
print("\n[4a] Purpose of type() function:")
print("The type() function is a built-in utility that returns the data type class of an object.")
print(f"Output for type(10)     : {type(10)}")
print(f"Output for type(10.5)   : {type(10.5)}")
print(f"Output for type(True)   : {type(True)}")
print(f"Output for type('hello'): {type('hello')}")

# --- 4(b) Operator Precedence ---
print("\n[4b] Operator Precedence Explanation:")
print("Operator Precedence determines the order of evaluation in an expression (BODMAS/PEMDAS).")
print("Evaluating expression: 3 + 4 * 2 ** 2 - 1")
print("1. Exponentiation (**): 2 ** 2 = 4  -> 3 + 4 * 4 - 1")
print("2. Multiplication (*):  4 * 4 = 16 -> 3 + 16 - 1")
print("3. Addition/Sub (L->R): 19 - 1     -> Result: 18")
print(f"Python verified calculation result : {3 + 4 * 2 ** 2 - 1}")

# --- 4(c) Loop Control Segments ---
print("\n[4c] Loop with 'continue' (skipping 5):")
for num in range(1, 11):
    if num == 5:
        continue
    print(num, end=" ")
print()

print("\n[4c] Loop with 'break' (stopping at 5):")
for num in range(1, 11):
    if num == 5:
        break
    print(num, end=" ")
print()


print("\n" + "="*50)
print("--- QUESTION 5: Functions & String Slicing ---")
print("="*50)

# --- 5 Theory ---
print("\n[5] Definition of a Function:")
print("A function is a reusable block of organized, self-contained code designed\n"
      "to perform a single, specific action when called, promoting modularity.")

print("\n[5i] String Slicing Syntax [start:stop:step]:")
print("- start : The starting index position where slice begins (inclusive).")
print("- stop  : The ending index position where slice terminates (exclusive).")
print("- step  : The increment value or character jumping stride interval.")

# --- 5(ii) Practical String Slices ---
s = "Python Programming"
print(f"\n[5ii] Target String: '{s}'")
print(f"Slice 1 ('Python')       : '{s[:6]}'")
print(f"Slice 2 ('Programming')  : '{s[7:]}'")
print(f"Slice 3 (Every 2nd char) : '{s[::2]}'")
print(f"Slice 4 (Reversed String): '{s[::-1]}'")

# --- 5 Math Module Demo ---
import math
print(f"\n[5] Math Module Demo (math.pi):")
print(f"The structural mathematical constant Pi is: {math.pi}")

# =====================================================================
# --- QUESTION 6: Pandas String Manipulation & Visualization ---
# =====================================================================

print("\n" + "="*50)
print("--- QUESTION 6: Pandas & Visualization ---")
print("="*50)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a mock dataset to simulate student records over time
data = {
    'Student_Name': ['SAMUEL OSUNBANWO', 'ALICE JOHNSON', 'BOB SMITH', 'CHIDI OBI', 'EMMA WATSON'],
    'Email': ['samuel@covenant.edu', 'alice@gmail.com', 'bob@yahoo.com', 'chidi@covenant.edu', 'emma@outlook.com'],
    'Math_Scores': [85, 62, 74, 45, 91],
    'Science_Scores': [89, 58, 80, 52, 95],
    'Marks_Over_Time_Term1': [70, 65, 72, 40, 85],
    'Marks_Over_Time_Term2': [78, 60, 75, 48, 88],
    'Marks_Over_Time_Term3': [85, 62, 74, 45, 91]
}

df = pd.DataFrame(data)

# --- Pandas String Functions ---
df['Student_Name_Lower'] = df['Student_Name'].str.lower()
df['Email_Domain'] = df['Email'].str.split('@').str[1]

print("\nProcessed DataFrame (Names lowercased & Domains extracted):")
print(df[['Student_Name_Lower', 'Email_Domain', 'Math_Scores', 'Science_Scores']])


# --- Visualization Plots ---
# Plot 1: Line plot of student marks over time
plt.figure(figsize=(6, 4))
terms = ['Term 1', 'Term 2', 'Term 3']
samuel_marks = [df.loc[0, 'Marks_Over_Time_Term1'], df.loc[0, 'Marks_Over_Time_Term2'], df.loc[0, 'Marks_Over_Time_Term3']]
plt.plot(terms, samuel_marks, marker='o', color='blue', linewidth=2)
plt.title("Student Marks Over Time (Samuel Osunbanwo)")
plt.xlabel("Academic Terms")
plt.ylabel("Marks Attained")
plt.grid(True)
plt.show()

# Plot 2: Histogram of marks distribution
plt.figure(figsize=(6, 4))
plt.hist(df['Math_Scores'], bins=4, color='green', edgecolor='black')
plt.title("Histogram of Overall Math Marks Distribution")
plt.xlabel("Marks Ranges")
plt.ylabel("Number of Students")
plt.show() 

# Plot 3: Scatter plot comparing Math vs Science scores
plt.figure(figsize=(6, 4))
plt.scatter(df['Math_Scores'], df['Science_Scores'], color='red', s=100, edgecolor='black')
plt.title("Scatter Plot: Math Scores vs. Science Scores")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.grid(True)
plt.show()


# =====================================================================
# --- QUESTION 7: Object-Oriented CGPA Classification ---
# =====================================================================

print("\n" + "="*50)
print("--- QUESTION 7: OOP CGPA Classification ---")
print("="*50)

# Instantiate 5 distinct student objects covering various tiers
student_database = [
    gu.AcademicRecord("Samuel Osunbanwo", "RUN/DTS/26/01", "DTS", 200, 4.85),
    gu.AcademicRecord("Alice Johnson",    "RUN/DTS/26/02", "DTS", 200, 4.20),
    gu.AcademicRecord("Bob Smith",        "RUN/DTS/26/03", "DTS", 200, 3.15),
    gu.AcademicRecord("Chidi Obi",         "RUN/DTS/26/04", "DTS", 200, 2.10),
    gu.AcademicRecord("Emma Watson",       "RUN/DTS/26/05", "DTS", 200, 1.35)
]

print("\nExecuting display_information() across the student objects:")
for student in student_database:
    student.display_information()