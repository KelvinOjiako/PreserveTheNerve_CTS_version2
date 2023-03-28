import serial


def instantiate_serial_communication(arduino_path: str, speed: int, timeout: int):
    serializer = RaspbianSerializer(arduino_path, speed, timeout)
    return serializer


def send_info_to_arduino():
    pass


def receive_info_from_arduino():
    pass


class RaspbianSerializer:
    def __init__(self, arduino_path: str, speed: int, timeout: int):
        self.ser = serial.Serial(arduino_path, speed, timeout)
        self.ser.reset_input_buffer()
        pass




    
