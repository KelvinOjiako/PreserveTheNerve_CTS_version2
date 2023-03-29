from guizero import App, PushButton
from GuiFrame.GuiTestManager import image_file_setup, experimental_main, move_to_next_widget, \
    move_to_previous_widget

from SerialCommunication.RaspberryPi.RaspianTwoWayCommunication import RaspbianSerializer, \
    receive_info_from_arduino, send_info_to_arduino, instantiate_serial_communication


def image_experiments():
    image_files = image_file_setup()
    app = App()
    manager = experimental_main(app, image_files)
    prev_button = PushButton(app, command=move_to_previous_widget, text="prev", args=[manager])
    next_button = PushButton(app, command=move_to_next_widget, text="next", args=[manager])
    app.display()


def serial_communication_test(arduino_path: str):
    speed: int = 9600
    time_out = 1
    ser = instantiate_serial_communication(arduino_path, speed, time_out)
    send_info_to_arduino(ser, "Message from Raspberry Pi Python!! ;)")
    arduino_output = receive_info_from_arduino(ser)
    string_output = f"The arduino message was {arduino_output}"
    print(string_output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = ""
    serial_communication_test(path)
