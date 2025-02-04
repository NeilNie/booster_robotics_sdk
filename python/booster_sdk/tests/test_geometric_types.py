
import unittest
import sys
sys.path.append("../")

# Import your wrapper classes
from datatypes.geometry import (
    Position,
    Orientation,
    Posture,
    Quaternion,
    Transform,
)

from booster_robotics_sdk_python import (
    Position as CppPosition,
    Orientation as CppOrientation,
    Posture as CppPosture,
    Quaternion as CppQuaternion,
    Transform as CppTransform,
)


# If your code is structured in a package, ensure the correct import path:
# from python_wrapper.wrapper import Position, Orientation, ... etc.

class TestPosition(unittest.TestCase):
    def test_init_default(self):
        """Test initializing a Position with default values."""
        p = Position()
        self.assertAlmostEqual(p.x, 0.0)
        self.assertAlmostEqual(p.y, 0.0)
        self.assertAlmostEqual(p.z, 0.0)

    def test_init_custom(self):
        """Test initializing a Position with custom values."""
        p = Position(1.5, -2.0, 3.0)
        self.assertAlmostEqual(p.x, 1.5)
        self.assertAlmostEqual(p.y, -2.0)
        self.assertAlmostEqual(p.z, 3.0)

    def test_from_cpp(self):
        """
        Test the from_cpp method using a mock C++ Pybind object.
        We pretend that the Pybind object has .x, .y, and .z attributes.
        """
        mock_cpp = CppPosition()
        mock_cpp.x = 10.0
        mock_cpp.y = 20.0
        mock_cpp.z = 30.0
        
        p = Position.from_cpp(mock_cpp)
        self.assertAlmostEqual(p.x, 10.0)
        self.assertAlmostEqual(p.y, 20.0)
        self.assertAlmostEqual(p.z, 30.0)

    def test_to_cpp(self):
        """
        Test the to_cpp method returns an instance of the underlying
        Pybind class. We'll check that the returned object's fields match.
        """
        p = Position(1.0, 2.0, 3.0)
        cpp_obj = p.to_cpp()
        # We check the attributes
        self.assertAlmostEqual(cpp_obj.x, 1.0)
        self.assertAlmostEqual(cpp_obj.y, 2.0)
        self.assertAlmostEqual(cpp_obj.z, 3.0)


class TestOrientation(unittest.TestCase):
    def test_init_default(self):
        o = Orientation()
        self.assertAlmostEqual(o.roll, 0.0)
        self.assertAlmostEqual(o.pitch, 0.0)
        self.assertAlmostEqual(o.yaw, 0.0)

    def test_init_custom(self):
        o = Orientation(roll=1.57, pitch=0.78, yaw=-3.14)
        self.assertAlmostEqual(o.roll, 1.57)
        self.assertAlmostEqual(o.pitch, 0.78)
        self.assertAlmostEqual(o.yaw, -3.14)

    def test_from_cpp(self):
        mock_cpp = CppOrientation()
        mock_cpp.roll = 0.1
        mock_cpp.pitch = 0.2
        mock_cpp.yaw = 0.3

        o = Orientation.from_cpp(mock_cpp)
        self.assertAlmostEqual(o.roll, 0.1)
        self.assertAlmostEqual(o.pitch, 0.2)
        self.assertAlmostEqual(o.yaw, 0.3)

    def test_to_cpp(self):
        o = Orientation(roll=0.1, pitch=0.2, yaw=0.3)
        cpp_obj = o.to_cpp()
        self.assertAlmostEqual(cpp_obj.roll, 0.1)
        self.assertAlmostEqual(cpp_obj.pitch, 0.2)
        self.assertAlmostEqual(cpp_obj.yaw, 0.3)


class TestQuaternion(unittest.TestCase):
    def test_default_init(self):
        q = Quaternion()
        self.assertAlmostEqual(q.x, 0.0)
        self.assertAlmostEqual(q.y, 0.0)
        self.assertAlmostEqual(q.z, 0.0)
        self.assertAlmostEqual(q.w, 1.0)

    def test_custom_init(self):
        q = Quaternion(0.1, 0.2, 0.3, 0.4)
        self.assertAlmostEqual(q.x, 0.1)
        self.assertAlmostEqual(q.y, 0.2)
        self.assertAlmostEqual(q.z, 0.3)
        self.assertAlmostEqual(q.w, 0.4)

    def test_from_cpp(self):
        mock_cpp = CppQuaternion()
        mock_cpp.x = 1.0
        mock_cpp.y = 2.0
        mock_cpp.z = 3.0
        mock_cpp.w = 4.0
        q = Quaternion.from_cpp(mock_cpp)
        self.assertAlmostEqual(q.x, 1.0)
        self.assertAlmostEqual(q.y, 2.0)
        self.assertAlmostEqual(q.z, 3.0)
        self.assertAlmostEqual(q.w, 4.0)

    def test_to_cpp(self):
        q = Quaternion(1.0, 2.0, 3.0, 4.0)
        cpp_obj = q.to_cpp()
        self.assertAlmostEqual(cpp_obj.x, 1.0)
        self.assertAlmostEqual(cpp_obj.y, 2.0)
        self.assertAlmostEqual(cpp_obj.z, 3.0)
        self.assertAlmostEqual(cpp_obj.w, 4.0)


if __name__ == '__main__':
    unittest.main()
