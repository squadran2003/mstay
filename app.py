from hotel import Hotel
from guest import Guest
from reservations import Reservation
import random

reservation_ids = []

def random_res_id():
    """this function will create a unique
    id filed for each reservation, the while loop
    is there to prevent duplicate id's been create"""

    num = random.randint(1, 1000)
    while len(reservation_ids) and num in reservation_ids:
        num = random.randint(1, 1000)
    reservation_ids.append(num)
    return num


def checkout(id, hotel):
    res = find_reservation(id, hotel.reservations)
    if res:
        print("{} has been checked out, the bill is {}".format(
            res.guest.name, res.bill
        ))
        hotel.reservations = [i for i in hotel.reservations if i.id != id]


def find_reservation(id, reservations):
    for r in reservations:
        if r.id==id:
            return r
    print("sorry could not find this reservation")


def clear_screen():
    """this function just clears
    screen"""
    print("*"*20)
    print("\n")


def help_text():
    print("\n")
    print("*"*20)
    print("USER GUIDE")
    print("*"*20)
    text = """
    Welcome to the hotel reservations
    app, please provide the required information
    as requested. Reservations dates should be
    in the format '%Y-%m-%d %H:%M:%S', default
    reservation time is for 1 day.


    Options
    make a reservation: R
    to list reservations: L
    show available rooms: LR [single room:1, double rooms:2, suites:3]
    for example to show all available single rooms enter LR1
    to quit the app its: Q
    show this help text its : H
    checkout is : C
    """

    print(text)
    print("*"*20)


def start():
    help_text()
    run = True
    hotel_name = None
    hotel_address = None
    hotel_created = False
    while run:
        if not hotel_name:
            hotel_name = input("Hotel name? ").upper()
        if not hotel_address:
            hotel_address = input("Hotel address? ").upper()
        if not hotel_name and not hotel_address:
            continue
        if not hotel_created:
            hotel = Hotel(hotel_name, hotel_address)
        hotel_created=True
        clear_screen()
        user_choice = input("What would you like to do? ").upper()
        if user_choice not in ['C','R','L','LR1','LR2','LR3','Q','H']:
            print("sorry dont recognise that choice!")
            continue
        if user_choice =='Q':
            clear_screen()
            print("Good bye!")
            run = False
        if user_choice == 'H':
            clear_screen()
            help_text()
        if user_choice == 'LR1':
            clear_screen()
            hotel.list_rooms(1)
        if user_choice == 'LR2':
            clear_screen()
            hotel.list_rooms(2)
        if user_choice == 'LR3':
            clear_screen()
            hotel.list_rooms(3)
        if user_choice == 'C':
            clear_screen()
            reservation_id = input("What is the reservation id? ")
            if not reservation_id:
                print("You did not enter a reservation id")
                continue
            checkout(int(reservation_id), hotel)
        if user_choice == 'R':
            clear_screen()
            guest_name = input("Name of the Guest? ")
            guest_address = input("Address ? ")
            guest_phone = input("Phone number? ")
            if not guest_name or not guest_address or not guest_phone:
                print("You missed some key guest information!")
                continue
            guest = Guest(guest_name, guest_address, guest_phone)
            clear_screen()
            print("What kind of room do you want to reserve?")
            room_type = input("1 for single, 2 for double, 3 for suite ")
            if not room_type:
                print("you did not enter a room type!")
                continue
            print("len of single rooms before the pop {}".format(len(hotel.single_bedrooms)))
            # get a room from the hotel
            if room_type == '1':
                if len(hotel.single_bedrooms)<1:
                    print("No single rooms available")
                    continue
                room = hotel.single_bedrooms.pop()
            if room_type == '2':
                if len(hotel.double_bedrooms)<1:
                    print("No double rooms available")
                    continue
                room = hotel.double_bedrooms.pop()
            if room_type == '3':
                if len(hotel.suites)<1:
                    print("No suites available")
                    continue
                room = hotel.suites.pop()
            print("how long will you be staying")
            date_from = input("From date? ")
            date_to = input("To date? ")
            if not date_from or not date_to:
                print(
                    """If you dont provide how long you will be staying,
                    we will assume you are staing a day""")
                res = Reservation(random_res_id(), guest, room)
            else:
                res = Reservation(
                        random_res_id(), guest, room, date_from, date_to
                )
            hotel.reservations.append(res)
            print("reservation made!")
            clear_screen()
        if user_choice =='L':
            clear_screen()
            hotel.list_reservations()




if __name__ == '__main__':
    start()
