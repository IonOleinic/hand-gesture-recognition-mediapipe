

class Menu:

    def __init__(self, name, items) -> None:
        self.name = name
        self.items = items
        self.selected_index = 0
        self.visibility = False

    def increaseIndex(self):
        self.selected_index += 1
        if self.selected_index >= len(self.items):
            self.selected_index = 0

    def decreaseIndex(self):
        self.selected_index -= 1
        if self.selected_index < 0:
            self.selected_index = len(self.items) - 1
