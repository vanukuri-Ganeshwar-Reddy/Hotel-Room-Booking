# billing.py

from data import bookings, rooms


def generate_bill():
    print("\n========== GENERATE BILL ==========")

    if len(bookings) == 0:
        print("No bookings available.")
        return

    name = input("Enter Customer Name: ").strip().lower()

    found = False

    for booking in bookings:
        if booking["name"].lower() == name:
            room = booking["room"]

            print("\n" + "=" * 40)
            print("          HOTEL BILL          ")
            print("=" * 40)
            print(f"Customer Name : {booking['name']}")
            print(f"Room Number   : {room}")
            print(f"Room Type     : {rooms[room]['type']}")
            print(f"Price/Day     : ₹{rooms[room]['price']}")
            print(f"Days Stayed   : {booking['days']}")
            print(f"Booking Date  : {booking['date']}")
            print("-" * 40)
            print(f"TOTAL AMOUNT  : ₹{booking['bill']}")
            print("=" * 40)

            found = True
            break

    if not found:
        print("❌ Booking not found.")