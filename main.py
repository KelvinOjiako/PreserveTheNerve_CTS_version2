
from guizero import App, PushButton
from GuiFrame.GuiTestManager import image_file_setup, experimental_main, move_to_next_widget, \
    move_to_previous_widget


def image_experiments():
    image_files = image_file_setup()
    app = App()
    manager = experimental_main(app, image_files)
    prev_button = PushButton(app, command=move_to_previous_widget, text="prev", args=[manager])
    next_button = PushButton(app, command=move_to_next_widget, text="next", args=[manager])
    app.display()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_experiments()
