class Monitor():
    count_monitor = 0

    def __init__(self, brand, size):
        Monitor.count_monitor += 1
        self._id_monitor = Monitor.count_monitor
        self._brand = brand
        self._size = size

    @property
    def id_monitor(self):
        return self._id_monitor

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    def __str__(self,):
        return (f"Id: {self.id_monitor}, Brand: {self.brand}, Size: {self.size} inches")


if __name__ == "__main__":
    monitor1 = Monitor("Dell", 15)
    print(monitor1)

    monitor2 = Monitor("Hp", 27)
    print(monitor2)
