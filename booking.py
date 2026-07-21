# booking.py

from data import rooms, bookings


def view_bookings():
    print("\n========== ALL BOOKINGS ==========")

    if len(bookings) == 0:
        print("No bookings found.")
        return

    for booking in bookings:
        print("-" * 40)
        print(f"Customer Name : {booking['name']}")
        print(f"Room Number   : {booking['room']}")
        print(f"Room Type     : {rooms[booking['room']]['type']}")
        print(f"Days          : {booking['days']}")
        print(f"Total Bill    : ₹{booking['bill']}")
        print(f"Booking Date  : {booking['date']}")
    print("-" * 40)


def search_booking():
    print("\n========== SEARCH BOOKING ==========")

    name = input("Enter Customer Name: ").strip().lower()

    found = False

    for booking in bookings:
        if booking["name"].lower() == name:
            print("\nBooking Found")
            print("-" * 30)
            print(f"Customer Name : {booking['name']}")
            print(f"Room Number   : {booking['room']}")
            print(f"Room Type     : {rooms[booking['room']]['type']}")
            print(f"Days          : {booking['days']}")
            print(f"Total Bill    : ₹{booking['bill']}")
            print(f"Booking Date  : {booking['date']}")
            found = True
            break

    if not found:
        print("❌ Booking not found.")


def cancel_booking():
    print("\n========== CANCEL BOOKING ==========")

    name = input("Enter Customer Name: ").strip().lower()

    for booking in bookings:
        if booking["name"].lower() == name:

            room_no = booking["room"]

            # Make the room available again
            rooms[room_no]["available"] = True

            # Remove the booking
            bookings.remove(booking)

            print("\n✅ Booking cancelled successfully!")
            print(f"Room {room_no} is now available.")
            return

    print("❌ Booking not found.")