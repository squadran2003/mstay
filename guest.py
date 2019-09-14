class Guest:
    id = None

    def __init__(self, name, address, phoneNumber):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    def __str__(self):
        print("{}\n {}\n {}\n {}\n".format(
            self.id, self.name, self.address, self.phoneNumber
        ))
