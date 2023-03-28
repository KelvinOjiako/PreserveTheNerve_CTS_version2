from guizero import Picture

"""
The GuiFrameManager Object is responsible for iterating across multiple UI
Widgets and activating the current widget while hiding all others.
    Makes use of 2 global functions: show_element & bury_element
    Member variables
    (*) gui_stack: The list that holds all gui elements
    (*) current_index: variable representing the current active element
    (*) size: The size of the gui_stack list
"""


def show_element(element):
    element.show()
    element.enable()


def bury_element(element):
    element.hide()
    element.disable()


def load_image_as_gui(main_App, full_file_path: str = None):
    picture_element = Picture(main_App, full_file_path)
    return picture_element


class GuiFrameManager:

    def __init__(self, gui_stack=list()):
        self.gui_stack = gui_stack
        self.current_index = 0

        if len(gui_stack) == 0:
            self.size = 0
        else:
            self.size = len(gui_stack)

    def deactivate_all_elements(self):
        for element in self.gui_stack:
            bury_element(element)

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def activate_current_element(self):
        if not self.empty():
            show_element(self.gui_stack[self.current_index])

    # Adds more GUI elements to the stack
    def append_stack_frame(self, more_gui_stack):
        self.gui_stack += more_gui_stack
        self.size += len(more_gui_stack)

    def activate_previous_element(self):
        if self.empty():
            print("Error!! An empty StackFrame CANT activate any elements")
        else:
            if self.current_index > 0:  # Ensures there's a previous element
                if 0 <= self.current_index < self.size:  # checks if current index is in correct range
                    bury_element(self.gui_stack[self.current_index])  # Hides current element
                    self.current_index -= 1  # moves to the previous element
                    self.activate_current_element()  # activates previous element
            else:
                print("Error! The gui Stack is at the beginning!! cannot activate a previous element.")

    def activate_next_element(self):
        if self.empty():
            print("Error!! An empty StackFrame CANT activate any elements")
        else:
            if self.current_index < self.size:
                # checks if there is a next element
                if 0 <= self.current_index < self.size - 1:  # ensures current_index is in the right range
                    bury_element(self.gui_stack[self.current_index])  # Hides the current element
                    self.current_index += 1  # moves to the next element
                    self.activate_current_element()  # activates the nest element
                else:
                    print("Error!! The gui stack is at the end. Cannot activate any other next element.")
            else:
                print("Error!! the guiStack is on its last frame. Add more Frames!")
