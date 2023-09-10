def input_students():
    student_list = []
    while True:
        name = input("Enter student name (or 'exit' to stop): ")
        if name.lower() == "exit":
            break
        roll_number = input("Enter roll number: ")
        cgpa = float(input("Enter CGPA: "))
        student = {"name": name, "roll_number": roll_number, "cgpa": cgpa}
        student_list.append(student)
    return student_list

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student['cgpa'], reverse=True)
    return sorted_students


#__main__
students = input_students()
sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")
