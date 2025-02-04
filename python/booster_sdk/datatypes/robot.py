from dataclasses import dataclass
from typing import Optional
from booster_robotics_sdk_python import GripperMotionParameter as CppGripperMotionParameter


@dataclass
class GripperMotionParameter:
    position: int = 0
    force: int = 0
    speed: int = 0

    @classmethod
    def from_cpp(cls, cpp_obj: CppGripperMotionParameter) -> "GripperMotionParameter":
        return cls(position=cpp_obj.position, force=cpp_obj.force, speed=cpp_obj.speed)

    def to_cpp(self) -> CppGripperMotionParameter:
        return CppGripperMotionParameter(self.position, self.force, self.speed)
