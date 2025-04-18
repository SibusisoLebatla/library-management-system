class WindowsButton:
    def render(self):
        return "Rendering Windows Button"

class MacOSButton:
    def render(self):
        return "Rendering MacOS Button"

class GUIFactory:
    def get_button(self):
        pass

class WindowsFactory(GUIFactory):
    def get_button(self):
        return WindowsButton()

class MacFactory(GUIFactory):
    def get_button(self):
        return MacOSButton()
