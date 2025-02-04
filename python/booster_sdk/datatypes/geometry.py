# python_wrapper/wrapper.py

from dataclasses import dataclass
from booster_robotics_sdk_python import GripperMotionParameter as CppGripperMotionParameter
from booster_robotics_sdk_python import Orientation as CppOrientation
from booster_robotics_sdk_python import Position as CppPosition
from booster_robotics_sdk_python import Posture as CppPosture
from booster_robotics_sdk_python import Quaternion as CppQuaternion
from booster_robotics_sdk_python import Transform as CppTransform


@dataclass
class Position:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @classmethod
    def from_cpp(cls, cpp_obj: CppPosition) -> "Position":
        """Create a Python Position from a C++ Pybind Position."""
        return cls(x=cpp_obj.x, y=cpp_obj.y, z=cpp_obj.z)

    def to_cpp(self) -> CppPosition:
        """Convert this Python Position into a C++ Pybind Position."""
        return CppPosition(self.x, self.y, self.z)


@dataclass
class Orientation:
    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0

    @classmethod
    def from_cpp(cls, cpp_obj: CppOrientation) -> "Orientation":
        return cls(roll=cpp_obj.roll, pitch=cpp_obj.pitch, yaw=cpp_obj.yaw)

    def to_cpp(self) -> CppOrientation:
        return CppOrientation(self.roll, self.pitch, self.yaw)


@dataclass
class Posture:
    position: Position
    orientation: Orientation

    @classmethod
    def from_cpp(cls, cpp_obj: CppPosture) -> "Posture":
        """Assuming cpp_obj.position and cpp_obj.orientation are themselves
        Pybind classes that map to C++ 'Position' and 'Orientation'."""
        return cls(position=Position.from_cpp(cpp_obj.position), orientation=Orientation.from_cpp(cpp_obj.orientation))

    def to_cpp(self) -> CppPosture:
        return CppPosture(self.position.to_cpp(), self.orientation.to_cpp())


@dataclass
class Quaternion:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0

    @classmethod
    def from_cpp(cls, cpp_obj: CppQuaternion) -> "Quaternion":
        return cls(x=cpp_obj.x, y=cpp_obj.y, z=cpp_obj.z, w=cpp_obj.w)

    def to_cpp(self) -> CppQuaternion:
        return CppQuaternion(self.x, self.y, self.z, self.w)


@dataclass
class Transform:
    position: Position
    orientation: Quaternion

    @classmethod
    def from_cpp(cls, cpp_obj: CppTransform) -> "Transform":
        return cls(position=Position.from_cpp(cpp_obj.position), orientation=Quaternion.from_cpp(cpp_obj.orientation))

    def to_cpp(self) -> CppTransform:
        return CppTransform(self.position.to_cpp(), self.orientation.to_cpp())
