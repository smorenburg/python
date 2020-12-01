class capibara:
    def __init__(self, name):
        self.name = name

    def my_name(self):
        print(self.name)
        return self.name


first_capibara = capibara("Robin")
second_capibara = capibara("Rayen")

first_capibara.my_name()
second_capibara.my_name()
