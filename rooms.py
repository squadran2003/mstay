class Room:
    available = True

    def __init__(self, id, number, room_type, price, currency):
        self.id = id
        self.number = number
        self.room_type = room_type
        self.price = price
        self.currency = currency
        self.reservation = None

    def __str__(self):
        print("Room id:{} Room no:{} Room Type:{} Price:{}{}".format(
            self.id, self.number, self.room_type, self.currency,self.price
        ))
