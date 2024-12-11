from keyboard import Keyboard
from mouse import Mouse
from monitor import Monitor


class Computer():
    computer_count = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_count += 1
        self._id_computer = Computer.computer_count
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    @property
    def id_computer(self):
        return self._id_computer

    @property
    def name(self):
        return self._name

    @property
    def monitor(self):
        return self._monitor

    @property
    def keyboard(self):
        return self._keyboard

    @property
    def mouse(self):
        return self._mouse

    def __str__(self):
        return f""" {self.name}: {self.id_computer}
        Monitor:{self.monitor}
        Keyboard:{self.keyboard}
        Mouse:{self.mouse}"""


if __name__ == "__main__":
    monitor1 = Monitor("Hp", 27)
    keyboard1 = Keyboard("Hp", "Usb")
    mouse1 = Mouse("Hp", "Usb")
    computer1 = Computer("Hp", monitor1, keyboard1, mouse1)
    print(computer1)

    monitor2 = Monitor("Gamer", 34)
    keyboard2 = Keyboard("Gamer", "Bluetooth")
    mouse2 = Mouse("Gamer", "Bluetooth")
    computer2 = Computer("Gamer", monitor2, keyboard2, mouse2)
    print(computer2)