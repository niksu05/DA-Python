class ClinicAppointment:
    def __init__(self):
        # Doctors with available slots
        self.doctors = ["Dr. Sharma", "Dr. Patel", "Dr. Mehta"]
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

        # Store appointments: {mobile: {patient_info, doctor, slot}}
        self.appointments = {}

        # Track slot bookings per doctor
        self.slot_bookings = {
            doctor: {slot: [] for slot in self.time_slots} for doctor in self.doctors
        }

    def book_appointment(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        mobile = input("Enter Mobile Number: ")

        # Prevent duplicate booking for same number
        if mobile in self.appointments:
            print("❌ Appointment already exists for this mobile number.")
            return

        print("\nAvailable Doctors:")
        for i, doctor in enumerate(self.doctors, 1):
            print(f"{i}. {doctor}")
        doctor_choice = int(input("Choose Doctor (1-3): ")) - 1
        if doctor_choice not in range(len(self.doctors)):
            print("❌ Invalid choice!")
            return
        doctor = self.doctors[doctor_choice]

        print("\nAvailable Time Slots:")
        for i, slot in enumerate(self.time_slots, 1):
            print(f"{i}. {slot}")
        slot_choice = int(input("Choose Time Slot (1-5): ")) - 1
        if slot_choice not in range(len(self.time_slots)):
            print("❌ Invalid choice!")
            return
        slot = self.time_slots[slot_choice]

        # Check if slot is full
        if len(self.slot_bookings[doctor][slot]) >= 3:
            print("❌ Slot is full for this doctor. Please choose another slot/doctor.")
            return

        # Save appointment
        self.appointments[mobile] = {
            "name": name,
            "age": age,
            "doctor": doctor,
            "slot": slot,
        }
        self.slot_bookings[doctor][slot].append(mobile)
        print(f"✅ Appointment booked successfully with {doctor} at {slot}.")

    def view_appointment(self):
        mobile = input("Enter Mobile Number: ")
        if mobile in self.appointments:
            appt = self.appointments[mobile]
            print("\n📋 Appointment Details:")
            print(f"Patient: {appt['name']} (Age: {appt['age']})")
            print(f"Doctor: {appt['doctor']}")
            print(f"Time Slot: {appt['slot']}")
        else:
            print("❌ No appointment found for this number.")

    def cancel_appointment(self):
        mobile = input("Enter Mobile Number: ")
        if mobile in self.appointments:
            appt = self.appointments.pop(mobile)
            self.slot_bookings[appt["doctor"]][appt["slot"]].remove(mobile)
            print("✅ Appointment cancelled successfully.")
        else:
            print("❌ No appointment found for this number.")

    def menu(self):
        while True:
            print("\n--- Clinic Appointment System ---")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                print("👋 Thank you for using Clinic Appointment System.")
                break
            else:
                print("❌ Invalid choice. Try again.")


# Run system
if __name__ == "__main__":
    clinic = ClinicAppointment()
    clinic.menu()
