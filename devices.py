import requests


class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.device_type = "Generic"
        self.actions = ["Power"]

    def send_power_req(self, status="OFF"):
        try:
            # result = requests.get(f"http://{self.ip}/cm?cmnd=POWER {status}")
            print(f"Power {status} sent to {self.name} ({self.ip})")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def __str__(self):
        return f"{self.name} at {self.ip}"


class SmartSwitch(Device):
    def __init__(self, name, ip):
        super().__init__(name, ip)
        self.device_type = "SmartSwitch"


class SmartSiren(Device):
    def __init__(self, name, ip):
        super().__init__(name, ip)
        self.device_type = "SmartSiren"


class SmartLed(Device):
    def __init__(self, name, ip):
        super().__init__(name, ip)
        self.device_type = "SmartLed"
        self.actions = ["Power", "Color"]

    def send_color_req(self, color):
        try:
            # result = requests.get(f"http://{self.ip}/cm?cmnd=Color {color}")
            print(f"Color {color} sent to {self.name} ({self.ip})")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
