from input_device import InputDevice


class Mouse(InputDevice):
    count_mouse = 0

    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        # self.brand = brand
        # self.input_type = input_type
        Mouse.count_mouse += 1
        self._id_mouse = Mouse.count_mouse

    @property
    def id_mouse(self):
        return self._id_mouse

    def __str__(self,):
        return (f" Id: {self.id_mouse}, Brand: {self.brand}, Input Type: {self.input_type} connection")


if __name__ == "__main__":
    mouse1 = Mouse("Hp", "USB")
    print(mouse1)

    mouse2 = Mouse("Acer", "Bluetooth")
    print(mouse2)