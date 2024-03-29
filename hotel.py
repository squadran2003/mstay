from rooms import Room
import random

room_ids = []

class Hotel:
    # hotel will have 52 rooms
        # 25 single rooms
        # 25 double rooms
        # 2 suites
    single_bedrooms = []
    double_bedrooms = []
    suites = []
    reservations = []
    # hotel will have 25 single bedrooms
    # hotel will have 25 double bedrooms
    # # hotel will have 2 suites
    # price of a single bed will be 90
    # price of a double bed will be 150
    # price of a suites will be 200
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.create_rooms()

    def generate_id(self):
        num = random.randint(1, 1000)
        while len(room_ids) and num in room_ids:
            num = random.randint(1, 1000)
        room_ids.append(num)
        return num

    def create_rooms(self):
        id = self.generate_id()
        for i in range(1, 26):
            self.single_bedrooms.append(Room(id, i, "single bed", 90, "£"))
        for i in range(1, 26):
            self.double_bedrooms.append(Room(id, i, "double bed",150,"£"))
        for i in range(1, 3):
            self.suites.append(Room(id,i, "suite", 200, "£"))

    def list_rooms(self, option):
        if option == 1:
            self.print_rooms(self.single_bedrooms)
        elif option == 2:
            self.print_rooms(self.double_bedrooms)
        else:
            self.print_rooms(self.suites)

    def list_reservations(self):
        print("list of reservations")
        print("-"*20)
        [r.__str__() for r in self.reservations]

    def print_rooms(self, rooms):
        for room in rooms:
            room.__str__()
