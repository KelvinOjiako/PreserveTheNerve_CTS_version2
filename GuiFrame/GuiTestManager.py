import os

from guizero import Box, Picture
from GuiFrame.GuiFrameManager import GuiFrameManager


def image_file_setup():
    full_path = r"C:\Users\kojia\PycharmProjects\PreserveTheNerveNCS\Images"
    library_computer_path = r"C:\Users\kso170000\PycharmProjects\PreserveTheNerve_CTS\Images"
    image_list = ["luffy_gif_test.gif", "1.GIF", "2.GIF", "1_1.GIF", "3.GIF", "3_1.GIF"]
    perfect_images = []

    for i in image_list:
        perfect_images.append(os.path.join(library_computer_path, i))
    return perfect_images


def experimental_main(main_app, image_files):
    # Creates 4 Box container UI Elements that will be rendered on the main_app
    welcome_container = Box(main_app, width=200, height=350, border=3)
    testing_container = Box(main_app, width=200, height=350, border=10)
    results_container = Box(main_app, width=200, height=350, border=15)
    export_container = Box(main_app, width=300, height=350, border=3)

    # A text box is then added to all the various Box Containers
    box1text = Picture(welcome_container, image=image_files[0])
    box2text = Picture(testing_container, image=image_files[1])
    box3text = Picture(results_container, image=image_files[2])
    box4text = Picture(export_container, image=image_files[3])

    # The box containers are then compiled together into a list
    widget_stack = [welcome_container, testing_container, results_container, export_container]
    # GuiFrame Object is created from list of Box containers
    manager_object = GuiFrameManager(widget_stack)
    manager_object.deactivate_all_elements()
    print(manager_object.size)
    manager_object.activate_current_element()
    return manager_object


# Triggers the GuiFrame to activate the next element and disable all other elements
def move_to_previous_widget(test_manager):
    test_manager.activate_previous_element()


# Triggers the previous element to be activated while disabling all else
def move_to_next_widget(test_manager):
    test_manager.activate_next_element()
