from dataclasses import dataclass
from dataclasses import field
from typing import List

from booster_robotics_sdk_python import GripperMotionParameter as CppGripperMotionParameter
from booster_robotics_sdk_python import ImuState as CppImuState
from booster_robotics_sdk_python import LowState as CppLowState
from booster_robotics_sdk_python import MotorCmd as CppMotorCmd
from booster_robotics_sdk_python import MotorState as CppMotorState
from constants.t1 import LowCmdType


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

@dataclass
class ImuState:
    """
    Placeholder for an IMU state wrapper. 
    Update fields/methods to reflect the actual C++ ImuState as needed.
    """
    # Example possible fields: (This is speculative)
    # orientation_w: float = 1.0
    # orientation_x: float = 0.0
    # orientation_y: float = 0.0
    # orientation_z: float = 0.0
    # ...

    @classmethod
    def from_cpp(cls, cpp_obj: CppImuState) -> "ImuState":
        """
        Convert from the C++ ImuState. 
        Fill in actual fields if you know them.
        """
        return cls()

    def to_cpp(self) -> CppImuState:
        """
        Convert this Python ImuState to a C++ ImuState.
        Fill in fields as appropriate.
        """
        return CppImuState()


@dataclass
class MotorState:
    mode: int = 0
    q: float = 0.0
    dq: float = 0.0
    ddq: float = 0.0
    tau_est: float = 0.0
    temperature: int = 0
    lost: int = 0
    # TODO: Check if this is the correct way to handle the reserve field
    # reserve is a std::array<uint32_t,2> in C++, so we treat it like a length-2 list in Python
    # reserve: List[int] = field(default_factory=lambda: [0, 0])

    @classmethod
    def from_cpp(cls, cpp_obj: CppMotorState) -> "MotorState":
        return cls(
            mode=cpp_obj.mode,
            q=cpp_obj.q,
            dq=cpp_obj.dq,
            ddq=cpp_obj.ddq,
            tau_est=cpp_obj.tau_est,
            temperature=cpp_obj.temperature,
            lost=cpp_obj.lost,
            # Convert the std::array<uint32_t, 2> to a Python list
            # reserve=list(cpp_obj.reserve)
        )

    def to_cpp(self) -> CppMotorState:
        # Create a fresh C++ MotorState and set properties
        c = CppMotorState()
        c.mode = self.mode
        c.q = self.q
        c.dq = self.dq
        c.ddq = self.ddq
        c.tau_est = self.tau_est
        c.temperature = self.temperature
        c.lost = self.lost
        # If the Pybind property accepts assigning a Python list, this should work.
        # Otherwise you might need to do something like:
        #   for i in range(2):
        #       c.reserve[i] = self.reserve[i]
        # c.reserve = self.reserve
        return c

    def __eq__(self, other: object) -> bool:
        """Compare via the underlying C++ operator==, if you want the same logic as C++."""
        if not isinstance(other, MotorState):
            return False
        return self.to_cpp() == other.to_cpp()


@dataclass
class LowState:
    # The C++ LowState references an ImuState and two vectors of MotorState.
    imu_state: ImuState = field(default_factory=ImuState)
    motor_state_parallel: List[MotorState] = field(default_factory=list)
    motor_state_serial: List[MotorState] = field(default_factory=list)

    @classmethod
    def from_cpp(cls, cpp_obj: CppLowState) -> "LowState":
        # Convert each piece
        imu = ImuState.from_cpp(cpp_obj.imu_state)
        # Convert each MotorState in the vectors
        parallel_py = [MotorState.from_cpp(ms) for ms in cpp_obj.motor_state_parallel]
        serial_py = [MotorState.from_cpp(ms) for ms in cpp_obj.motor_state_serial]

        return cls(
            imu_state=imu,
            motor_state_parallel=parallel_py,
            motor_state_serial=serial_py
        )

    def to_cpp(self) -> CppLowState:
        c = CppLowState()
        # NOTE: .imu_state in the C++ binding is settable with a const ImuState&.
        c.imu_state = self.imu_state.to_cpp()
        # The pybind property wants a std::vector<MotorState>, so we pass in a list of CppMotorState
        c.motor_state_parallel = [ms.to_cpp() for ms in self.motor_state_parallel]
        c.motor_state_serial = [ms.to_cpp() for ms in self.motor_state_serial]
        return c

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LowState):
            return False
        return self.to_cpp() == other.to_cpp()


@dataclass
class MotorCmd:
    mode: int = 0
    q: float = 0.0
    dq: float = 0.0
    tau: float = 0.0
    kp: float = 0.0
    kd: float = 0.0
    weight: float = 0.0

    @classmethod
    def from_cpp(cls, cpp_obj: CppMotorCmd) -> "MotorCmd":
        return cls(
            mode=cpp_obj.mode,
            q=cpp_obj.q,
            dq=cpp_obj.dq,
            tau=cpp_obj.tau,
            kp=cpp_obj.kp,
            kd=cpp_obj.kd,
            weight=cpp_obj.weight,
        )

    def to_cpp(self) -> CppMotorCmd:
        c = CppMotorCmd()
        c.mode = self.mode
        c.q = self.q
        c.dq = self.dq
        c.tau = self.tau
        c.kp = self.kp
        c.kd = self.kd
        c.weight = self.weight
        return c

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MotorCmd):
            return False
        return self.to_cpp() == other.to_cpp()


class LowCmd:
    def __init__(self, num_joints: int, cmd_type: LowCmdType):
        self.cmd_type: LowCmdType = cmd_type
        self.motor_cmd: list[MotorCmd] = [MotorCmd() for _ in range(num_joints)]
