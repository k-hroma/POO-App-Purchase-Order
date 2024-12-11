class InputDevice():
    def __init__(self, brand, input_type):
        self._brand = brand
        self._input_type = input_type

    @property
    def brand(self):
        return self._brand

    @property
    def input_type(self):
        return self._input_type
