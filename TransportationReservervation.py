class BusReservation:
    def __init__(self):

        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Mysore": 400,
            "Chennai to Coimbatore": 700
        }

        self.tickets = {}
        self.next_ticket_id = 1

        self.seats = {route: [] for route in self.routes}

    def show_routes(self):
        print("\n🚌 Available Routes:")
        for i, (route, price) in enumerate(self.routes.items(), 1):
            print(f"{i}. {route} - ₹{price}")

    def book_ticket(self):
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile Number: ")

        if not (mobile.isdigit() and len(mobile) == 10):
            print("❌ Invalid Mobile Number! Must be 10 digits.")
            return

        self.show_routes()
        route_choice = int(input("Choose Route (1–4): ")) - 1

        if route_choice not in range(len(self.routes)):
            print("❌ Invalid route choice!")
            return

        route = list(self.routes.keys())[route_choice]

        if len(self.seats[route]) >= 40:
            print("❌ Sorry! No seats available on this route.")
            return

        seat_no = len(self.seats[route]) + 1
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "price": self.routes[route]
        }

        self.seats[route].append(seat_no)

        print(
            f"✅ Ticket Booked Successfully! Ticket ID: {ticket_id}, Seat No: {seat_no}")

    def view_ticket(self):
        ticket_id = int(input("Enter Ticket ID: "))
        if ticket_id in self.tickets:
            t = self.tickets[ticket_id]
            print("\n📋 Ticket Details:")
            print(f"Ticket ID: {ticket_id}")
            print(f"Passenger: {t['name']} (Age: {t['age']})")
            print(f"Mobile: {t['mobile']}")
            print(f"Route: {t['route']} - ₹{t['price']}")
            print(f"Seat No: {t['seat']}")
        else:
            print("❌ Ticket not found.")

    def cancel_ticket(self):
        ticket_id = int(input("Enter Ticket ID to Cancel: "))
        if ticket_id in self.tickets:
            t = self.tickets.pop(ticket_id)
            self.seats[t["route"]].remove(t["seat"])
            print("✅ Ticket cancelled successfully.")
        else:
            print("❌ Ticket not found.")

    def menu(self):
        while True:
            print("\n--- Bus Reservation System ---")
            print("1. Show Available Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_ticket()
            elif choice == "4":
                self.cancel_ticket()
            elif choice == "5":
                print("👋 Thank you for using Bus Reservation System.")
                break
            else:
                print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    bus = BusReservation()
    bus.menu()
