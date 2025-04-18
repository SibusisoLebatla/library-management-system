import unittest
from creational_patterns.prototype import ShapeCache, Circle

class TestPrototypePattern(unittest.TestCase):
    def test_clone_circle(self):
        ShapeCache.load_cache()
        circle1 = ShapeCache.get_shape("circle")
        circle2 = ShapeCache.get_shape("circle")
        self.assertEqual(circle1.radius, circle2.radius)
        self.assertIsNot(circle1, circle2)
