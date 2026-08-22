# 3. Digital Student Gradebook
# Key Concepts:Attributes holding collections (lists/dictionaries), Instance Methods, Logic calculations inside classes.
# Goal:Create a `Student` class that stores grades in a list. Write methods to `add_grade()`, calculate the average, and determine a pass/fail status based on threshold logic.

class StudentGradebook:
    _grade_type = ["O", "A+", "A", "B+", "B", "C+", "C", "D+", "D", 'F']
    _grade_values = { "O":10, "A+":9, "A":8, "B+":7, "B":6, "C+":5, "C":4, "D+":3, "D":2, "F":"Fail"}
    _point_values = {10:"O", 9:"A+", 8:"A", 7:"B+", 6:"B", 5:"C+", 4:"C", 3:"D+", 2:"D"}

    def __init__(self, name:str):
        self.name = name
        self.__grades = {}

    def help(self):
            print(f"""Following are grades with there associated values.
    {StudentGradebook._grade_values}""")

    #{"hindi":"A", "Marathi":A+, "Maths":"C"}
    def add_grade(self, grades:dict):
        for subject, grade in grades.items():
            subject = subject.upper()
            grade = grade.upper()
            if grade not in StudentGradebook._grade_type:
                print(f"Invalid Grade: {grade}, use help() method to get grade scheme")
                return 0
            else:
                self.__grades[subject] = grade
                continue
        return 1


    def get_grades(self):
        return self.__grades

    def result(self) -> str:

        failed_subjects = []
        for subject, grade in self.__grades.items():
            if grade == "F":
                failed_subjects.append(subject)
        if failed_subjects:
            return f'Failed. Subjects:{failed_subjects}'

        grade_sum = 0
        for subject, grade in self.__grades.items():
            grade_sum += StudentGradebook._grade_values[grade]
        try:
            result = round(grade_sum/len(self.__grades))
        except ZeroDivisionError:
            return "Kindly Add Grades to a Student Gradebook."

        return f'Grade:"{StudentGradebook._point_values[result]}". Result: Passed!'



# Example:
darsh_gradebook = StudentGradebook("Darsh")
darsh_gradebook.add_grade({"Hindi":"D", "English":"D", "Maths":"D", "Science":"D"})
print(darsh_gradebook.result())
