class PurchaseOrder():
    count_order = 0

    def __init__(self, computers):
        PurchaseOrder.count_order += 1
        self.id_order = PurchaseOrder.count_order
        self.computers = computers

    def add_computer(self, computer):
        self.computer = computer
        self.computers.append(computer)

    def __str__(self):
        computers_str = ""
        for computer in self.computers:
            computers_str += "\n" + computer.__str__()
        return f"""Purchase Order: {self.id_order}
        Computers: {computers_str}
        """
