import unittest
from creational_patterns.abstract_factory.factory import GUIFactory

class TestAbstractFactory(unittest.TestCase):
    def test_windows_ui(self):
        factory = GUIFactory.get_factory("windows")
        button = factory.create_button()
        self.assertEqual(button.click(), "Windows Button clicked")

    def test_mac_ui(self):
        factory = GUIFactory.get_factory("mac")
        button = factory.create_button()
        self.assertEqual(button.click(), "Mac Button clicked")
