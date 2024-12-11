from computer import Computer
from keyboard import Keyboard
from monitor import Monitor
from mouse import Mouse
from purchase_order import PurchaseOrder

print("***Purchase Pc Order App***")
# Computer 1
monitor1 = Monitor("Hp", 27)
keyboard1 = Keyboard("Hp", "Usb")
mouse1 = Mouse("Hp", "Usb")
computer1 = Computer("Hp", monitor1, keyboard1, mouse1)

# Computer 2
monitor2 = Monitor("Gamer", 34)
keyboard2 = Keyboard("Gamer", "Bluetooth")
mouse2 = Mouse("Gamer", "Bluetooth")
computer2 = Computer("Gamer", monitor2, keyboard2, mouse2)

# Computer 3
monitor3 = Monitor("Dell", 27)
keyboard3 = Keyboard("Dell", "Bluetooth")
mouse3 = Mouse("Dell", "Bluetooth")
computer3 = Computer("Dell", monitor3, keyboard3, mouse3)

# Computer List
computers1 = [computer1, computer2]
order1 = PurchaseOrder(computers1)
order1.add_computer(computer3)
print(order1)