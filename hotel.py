# hotel.py

from data import rooms, bookings
from datetime import datetime


def view_rooms():
    print("\n========== AVAILABLE ROOMS ==========")

    found = False

    for room_no, details in rooms.items():
        if details["available"]:
            print(f"\nRoom No : {room_no}")
            print(f"Room Type : {details['type']}")
            print(f"Price per Day : ₹{details['price']}")
            print("Status : Available")
            found = True

    if not found:
        print("\nNo rooms are available.")


def book_room():
    print("\n========== BOOK ROOM ==========")

    name = input("Enter Customer Name: ")

    try:
        room_no = int(input("Enter Room Number: "))
        days = int(input("Enter Number of Days: "))

        if room_no not in rooms:
            print("\n❌ Invalid Room Number.")
            return

        if not rooms[room_no]["available"]:
            print("\n❌ Room is already booked.")
            return

        total_bill = rooms[room_no]["price"] * days

        booking = {
            "name": name,
            "room": room_no,
            "days": days,
            "bill": total_bill,
            "date": datetime.now().strftime("%d-%m-%Y")
        }

        bookings.append(booking)

        rooms[room_no]["available"] = False

        print("\n✅ Room booked successfully!")
        print(f"Customer : {name}")
        print(f"Room No : {room_no}")
        print(f"Total Bill : ₹{total_bill}")

    except ValueError:
        print("\n❌ Please enter valid numeric values.")