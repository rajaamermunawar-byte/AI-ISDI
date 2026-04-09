class AdmissionForm:
    def __init__(self, college_name="ABC College"):
        self.college_name = college_name
        self.students = []
    
    def set_college_name(self, name):
        self.college_name = name
    
    def add_student(self):
        print("\n--- Student Admission Form ---")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        roll_no = input("Enter Roll No: ")
        marks = input("Enter Marks: ")
        
        student_data = {
            "name": name,
            "age": age,
            "roll_no": roll_no,
            "marks": marks
        }
        self.students.append(student_data)
        print("Admission successful!")
    
    def print_form(self, student_index):
        if student_index >= len(self.students):
            print("Invalid student index!")
            return
        
        student = self.students[student_index]
        print("\n" + "="*60)
        print(f"{'STUDENT ADMISSION FORM':^60}")
        print(f"{'Institution: ' + self.college_name:^60}")
        print("="*60)
        print(f"Name of Student:        {student['name'].upper()}")
        print(f"Age:                    {student['age']} years")
        print(f"Roll No:                {student['roll_no']}")
        print(f"Marks:                  {student['marks']}")
        print("="*60 + "\n")
    
    def print_enrollment_summary(self):
        print("\n" + "="*75)
        print(f"{'ENROLLMENT SUMMARY REPORT':^75}")
        print(f"{'Institution: ' + self.college_name:^75}")
        print("="*75)
        print(f"Total Students Enrolled: {len(self.students)}")
        
        print(f"{'Name':<20} {'Age':<6} {'Roll No':<12} {'Marks':<12}")
        print("-"*75)
        
        for student in self.students:
            print(f"{student['name']:<20} {student['age']:<6} {student['roll_no']:<12} {student['marks']:<12}")
        
        print("="*75 + "\n")

# Example usage
admission = AdmissionForm("XYZ University")

admission.add_student()

admission.print_form(0)

admission.print_enrollment_summary()
