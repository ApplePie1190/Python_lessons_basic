class OfficeEquipment:
    def __init__(self, brand, serial):
        self.brand = brand
        self.serial = serial


class Printer(OfficeEquipment):
    def __init__(self, brand, serial, is_color):
        super().__init__(brand, serial)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, brand, serial, format):
        super().__init__(brand, serial)
        self.format = format


class Copier(OfficeEquipment):
    def __init__(self, brand, serial, dpi):
        super().__init__(brand, serial)
        self.dpi = dpi


class Warehouse:
    devices_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    devices_in_office = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def send_warehouse(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
        print(device.__class__.__name__, device.brand, device.serial, 'Принято на склад.')

    @classmethod
    def send_office(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].remove(device)
        cls.devices_in_office[str(device.__class__.__name__)].append(device)
        print(device.__class__.__name__, device.brand, device.serial, 'Передано в офис.')


scanner_1 = Scanner('HP', '123123', 'A4')
scanner_2 = Scanner('Asus', '123000', 'A5')
printer_1 = Printer('Lenovo', '000111', True)
printer_2 = Printer('HP', '777777', False)
copier_1 = Copier('Asus', '010101', 360)
copier_2 = Copier('ZTE', '454545', 1024)
Warehouse.send_warehouse(scanner_1)
Warehouse.send_warehouse(scanner_2)
Warehouse.send_warehouse(printer_1)
Warehouse.send_warehouse(printer_2)
Warehouse.send_office(scanner_1)
