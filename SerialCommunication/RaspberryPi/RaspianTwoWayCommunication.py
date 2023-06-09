import serial
import time


def instantiate_serial_communication(arduino_path: str, speed: int, timeout_setting: int):
    serializer = RaspbianSerializer(arduino_path, speed, timeout_setting)
    return serializer


def send_info_to_arduino(serializer, info_to_send):
    binary_string = bytes(info_to_send, 'utf-8')
    serializer.ser.write(binary_string)


def receive_info_from_arduino(serializer: serial.Serial):
    if serializer.ser.in_waiting > 0:
        return serializer.ser.readline().decode('utf-8').rstrip()


class RaspbianSerializer:
    def __init__(self, arduino_path: str, speed: int, timing: int):
        self.ser = serial.Serial(arduino_path, speed, timeout=1)
        self.ser.reset_input_buffer()
        pass
