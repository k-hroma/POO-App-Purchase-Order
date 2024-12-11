from input_device import InputDevice


class Keyboard(InputDevice):
    count_keyboard = 0

    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        # self.brand = brand
        # self.input_type = input_type
        Keyboard.count_keyboard += 1
        self._id_keyboard = Keyboard.count_keyboard

    @property
    def id_keyboard(self):
        return self._id_keyboard

    def __str__(self,):
        return (f" Id: {self.id_keyboard}, Brand: {self.brand}, Input Type: {self.input_type} connection")


if __name__ == "__main__":
    Keyboard1 = Keyboard("Hp", "USB")
    print(Keyboard1)

    Keyboard2 = Keyboard("Acer", "Bluetooth")
    print(Keyboard2)
