class student:
    def __init__(self,name):
        self.st_name=name.capitalize()
    print("Please Enter The Student Detail")
    def st_data(self):
        self.course=input("Enter the Course Name").capitalize()
        self.branch=input("Enter the branch Name").capitalize()
        self.roll_no=int(input("Enter Roll No."))
        self.year=int(input("Enter your year."))
class student_bg(student):
    def __init__(self):
        super().__init__(input("Enter your name: "))  # Call base class constructor for name
        self.father=input("Father's name=").capitalize()
        self.mother=input("Mother's name=").capitalize()
        self.add=input("address=").capitalize()
    def show(self):
        print()
        print("Student Details:")
        print(f"Name: {self.st_name}")
        print(f"Course: {self.course}")
        print(f"Branch: {self.branch}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Year: {self.year}")
        print("\nFamily Details:")
        print(f"Father's Name: {self.father}")
        print(f"Mother's Name: {self.mother}")
        print(f"Address: {self.add}")

stu1=student_bg()
stu1.st_data()
stu1.show()
    