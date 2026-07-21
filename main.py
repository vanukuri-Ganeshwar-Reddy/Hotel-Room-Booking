# main.py

from hotel import view_rooms, book_room
from booking import view_bookings, search_booking, cancel_booking
from billing import generate_bill


def menu():
    while True:
        print("\n" + "=" * 40)
        print("     HOTEL ROOM BOOKING SYSTEM")
        print("=" * 40)
        print("1. View Available Rooms")
        print("2. Book Room")
        print("3. View Bookings")
        print("4. Search Booking")
        print("5. Cancel Booking")
        print("6. Generate Bill")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            view_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            search_booking()

        elif choice == "5":
            cancel_booking()

        elif choice == "6":
            generate_bill()

        elif choice == "7":
            print("\nThank you for using Hotel Room Booking System!")
            print("Visit Again!\n")
            break

        else:
            print("\n❌ Invalid Choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    menu()