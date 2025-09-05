class SchoolManagement:
    def __init__(self):
        self.students = {}

    def new_admission(self):
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        std_class = int(input("Enter Class (1–12): "))
        mobile = input("Enter Guardian Mobile Number: ")

        if age < 5 or age > 18:
            print("❌ Invalid Age! Age must be between 5 and 18.")
            return

        if not (mobile.isdigit() and len(mobile) == 10):
            print("❌ Invalid Mobile Number! Must be 10 digits.")
            return

        student_id = self.next_id
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": std_class,
            "mobile": mobile
        }
        self.next_id += 1

        print(f"✅ Admission successful! Assigned Student ID: {student_id}")

    def view_student(self):
        student_id = int(input("Enter Student ID: "))
        if student_id in self.students:
            data = self.students[student_id]
            print("\n📋 Student Details:")
            print(f"ID: {student_id}")
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Class: {data['class']}")
            print(f"Guardian Mobile: {data['mobile']}")
        else:
            print("❌ No record found for this Student ID.")

    def update_student(self):
        student_id = int(input("Enter Student ID to Update: "))
        if student_id in self.students:
            print("\nUpdate Options:")
            print("1. Update Class")
            print("2. Update Mobile Number")
            choice = input("Enter choice: ")

            if choice == "1":
                new_class = int(input("Enter New Class (1–12): "))
                self.students[student_id]["class"] = new_class
                print("✅ Class updated successfully.")
            elif choice == "2":
                new_mobile = input("Enter New Mobile Number: ")
                if new_mobile.isdigit() and len(new_mobile) == 10:
                    self.students[student_id]["mobile"] = new_mobile
                    print("✅ Mobile Number updated successfully.")
                else:
                    print("❌ Invalid Mobile Number!")
            else:
                print("❌ Invalid choice.")
        else:
            print("❌ Student ID not found.")

    def remove_student(self):
        student_id = int(input("Enter Student ID to Remove: "))
        if student_id in self.students:
            self.students.pop(student_id)
            print("✅ Student record removed successfully.")
        else:
            print("❌ Student ID not found.")

    def menu(self):
        while True:
            print("\n--- School Management System ---")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.new_admission()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("👋 Exiting School Management System. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    school = SchoolManagement()
    school.menu()
