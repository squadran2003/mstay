import datetime
from datetime import timedelta

# default reservation period is 1 day
default_period = (datetime.datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
date_today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Reservation:
    bill = 0

    def __init__(self, id, guest, room, date_from=default_period, date_to=date_today):
        self.id = id
        self.guest = guest
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.calculate_bill()

    def calculate_bill(self):
        # this function will have to change to figure out
        # how  many days a guest has stayed
        if self.valid_date(self.date_from) and self.valid_date(self.date_to):
            date_from = datetime.datetime.strptime(self.date_from,'%Y-%m-%d %H:%M:%S')
            date_to = datetime.datetime.strptime(self.date_to,'%Y-%m-%d %H:%M:%S')
            if (date_to - date_from)<=timedelta(days=1):
                self.bill = self.room.price
            else:
                self.bill = self.room.price * 2
        else:
            print("Invalid date format, should be '%Y-%m-%d %H:%M:%S'")

    def valid_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        except:
            return False
        else:
            return True

    def __str__(self):
        print("id:{} Guest name:{} Room Number:{} Room Type:{} from:{} to:{} Total:{}{}".format(
            self.id, self.guest.name, str(self.room.number),self.room.room_type,
            self.date_from, self.date_to, self.room.currency,str(self.bill)
        ))
