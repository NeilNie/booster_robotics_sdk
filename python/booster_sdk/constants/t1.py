from enum import Enum

from booster_robotics_sdk_python import B1HandAction as ImportedB1HandAction
from booster_robotics_sdk_python import B1HandIndex as ImportedB1HandIndex
from booster_robotics_sdk_python import B1JointCnt as ImportedB1JointCnt
from booster_robotics_sdk_python import B1JointCnt7DofArm as ImportedB1jointCnt7DofArm
from booster_robotics_sdk_python import B1JointIndex as ImportedB1JointIndex
from booster_robotics_sdk_python import B1JointIndexWith7DofArm as ImportedB1JointIndexWith7DofArm
from booster_robotics_sdk_python import B1LocoApiId as ImportedB1LocoApiId
from booster_robotics_sdk_python import Frame as ImportedFrame
from booster_robotics_sdk_python import GripperControlMode as ImportedGripperControlMode
from booster_robotics_sdk_python import RobotMode as ImportedRobotMode


class RobotMode(Enum):
    UNKNOWN = ImportedRobotMode.kUnknown
    DAMPING = ImportedRobotMode.kDamping
    PREPARE = ImportedRobotMode.kPrepare
    WALKING = ImportedRobotMode.kWalking
    CUSTOM = ImportedRobotMode.kCustom


class B1JointIndex(Enum):
    HEAD_YAW = ImportedB1JointIndex.kHeadYaw
    HEAD_PITCH = ImportedB1JointIndex.kHeadPitch
    LEFT_SHOULDER_PITCH = ImportedB1JointIndex.kLeftShoulderPitch
    LEFT_SHOULDER_ROLL = ImportedB1JointIndex.kLeftShoulderRoll
    LEFT_ELBOW_PITCH = ImportedB1JointIndex.kLeftElbowPitch
    LEFT_ELBOW_YAW = ImportedB1JointIndex.kLeftElbowYaw
    RIGHT_SHOULDER_PITCH = ImportedB1JointIndex.kRightShoulderPitch
    RIGHT_SHOULDER_ROLL = ImportedB1JointIndex.kRightShoulderRoll
    RIGHT_ELBOW_PITCH = ImportedB1JointIndex.kRightElbowPitch
    RIGHT_ELBOW_YAW = ImportedB1JointIndex.kRightElbowYaw
    WAIST = ImportedB1JointIndex.kWaist
    LEFT_HIP_PITCH = ImportedB1JointIndex.kLeftHipPitch
    LEFT_HIP_ROLL = ImportedB1JointIndex.kLeftHipRoll
    LEFT_HIP_YAW = ImportedB1JointIndex.kLeftHipYaw
    LEFT_KNEE_PITCH = ImportedB1JointIndex.kLeftKneePitch
    CRANK_UP_LEFT = ImportedB1JointIndex.kCrankUpLeft
    CRANK_DOWN_LEFT = ImportedB1JointIndex.kCrankDownLeft
    RIGHT_HIP_PITCH = ImportedB1JointIndex.kRightHipPitch
    RIGHT_HIP_ROLL = ImportedB1JointIndex.kRightHipRoll
    RIGHT_HIP_YAW = ImportedB1JointIndex.kRightHipYaw
    RIGHT_KNEE_PITCH = ImportedB1JointIndex.kRightKneePitch
    CRANK_UP_RIGHT = ImportedB1JointIndex.kCrankUpRight
    CRANK_DOWN_RIGHT = ImportedB1JointIndex.kCrankDownRight


class B1JointIndexWith7DofArm(Enum):
    HEAD_YAW = ImportedB1JointIndexWith7DofArm.kHeadYaw
    HEAD_PITCH = ImportedB1JointIndexWith7DofArm.kHeadPitch
    LEFT_SHOULDER_PITCH = ImportedB1JointIndexWith7DofArm.kLeftShoulderPitch
    LEFT_SHOULDER_ROLL = ImportedB1JointIndexWith7DofArm.kLeftShoulderRoll
    LEFT_ELBOW_PITCH = ImportedB1JointIndexWith7DofArm.kLeftElbowPitch
    LEFT_ELBOW_YAW = ImportedB1JointIndexWith7DofArm.kLeftElbowYaw
    LEFT_WRIST_PITCH = ImportedB1JointIndexWith7DofArm.kLeftWristPitch
    LEFT_WRIST_YAW = ImportedB1JointIndexWith7DofArm.kLeftWristYaw
    LEFT_HAND_ROLL = ImportedB1JointIndexWith7DofArm.kLeftHandRoll
    RIGHT_SHOULDER_PITCH = ImportedB1JointIndexWith7DofArm.kRightShoulderPitch
    RIGHT_SHOULDER_ROLL = ImportedB1JointIndexWith7DofArm.kRightShoulderRoll
    RIGHT_ELBOW_PITCH = ImportedB1JointIndexWith7DofArm.kRightElbowPitch
    RIGHT_ELBOW_YAW = ImportedB1JointIndexWith7DofArm.kRightElbowYaw
    RIGHT_WRIST_PITCH = ImportedB1JointIndexWith7DofArm.kRightWristPitch
    RIGHT_WRIST_YAW = ImportedB1JointIndexWith7DofArm.kRightWristYaw
    RIGHT_HAND_ROLL = ImportedB1JointIndexWith7DofArm.kRightHandRoll
    WAIST = ImportedB1JointIndexWith7DofArm.kWaist
    LEFT_HIP_PITCH = ImportedB1JointIndexWith7DofArm.kLeftHipPitch
    LEFT_HIP_ROLL = ImportedB1JointIndexWith7DofArm.kLeftHipRoll
    LEFT_HIP_YAW = ImportedB1JointIndexWith7DofArm.kLeftHipYaw
    LEFT_KNEE_PITCH = ImportedB1JointIndexWith7DofArm.kLeftKneePitch
    CRANK_UP_LEFT = ImportedB1JointIndexWith7DofArm.kCrankUpLeft
    CRANK_DOWN_LEFT = ImportedB1JointIndexWith7DofArm.kCrankDownLeft
    RIGHT_HIP_PITCH = ImportedB1JointIndexWith7DofArm.kRightHipPitch
    RIGHT_HIP_ROLL = ImportedB1JointIndexWith7DofArm.kRightHipRoll
    RIGHT_HIP_YAW = ImportedB1JointIndexWith7DofArm.kRightHipYaw
    RIGHT_KNEE_PITCH = ImportedB1JointIndexWith7DofArm.kRightKneePitch
    CRANK_UP_RIGHT = ImportedB1JointIndexWith7DofArm.kCrankUpRight
    CRANK_DOWN_RIGHT = ImportedB1JointIndexWith7DofArm.kCrankDownRight


class B1LocoApiId(Enum):
    CHANGE_MODE = ImportedB1LocoApiId.kChangeMode
    MOVE = ImportedB1LocoApiId.kMove
    ROTATE_HEAD = ImportedB1LocoApiId.kRotateHead


class B1HandAction(Enum):
    HAND_OPEN = ImportedB1HandAction.kHandOpen
    HAND_CLOSE = ImportedB1HandAction.kHandClose


class B1HandIndex(Enum):
    LEFT_HAND = ImportedB1HandIndex.kLeftHand
    RIGHT_HAND = ImportedB1HandIndex.kRightHand


class GripperControlMode(Enum):
    POSITION = (
        ImportedGripperControlMode.kPosition
    )  # Position mode: stops at target position or specified reaction force
    FORCE = (
        ImportedGripperControlMode.kForce
    )  # Force mode: continues to move with specified force if target position is not reached


class Frame(Enum):
    UNKNOWN = ImportedFrame.kUnknown
    BODY = ImportedFrame.kBody
    HEAD = ImportedFrame.kHead
    LEFT_HAND = ImportedFrame.kLeftHand
    RIGHT_HAND = ImportedFrame.kRightHand
    LEFT_FOOT = ImportedFrame.kLeftFoot
    RIGHT_FOOT = ImportedFrame.kRightFoot


B1_JOINT_CNT_7_DOF_ARM = ImportedB1jointCnt7DofArm
B1_JOINT_CNT = ImportedB1JointCnt

B1_JOINTS_7_DOF_ARM = [
    B1JointIndexWith7DofArm.LEFT_SHOULDER_PITCH,
    B1JointIndexWith7DofArm.LEFT_SHOULDER_ROLL,
    B1JointIndexWith7DofArm.LEFT_ELBOW_PITCH,
    B1JointIndexWith7DofArm.LEFT_ELBOW_YAW,
    B1JointIndexWith7DofArm.LEFT_WRIST_PITCH,
    B1JointIndexWith7DofArm.LEFT_WRIST_YAW,
    B1JointIndexWith7DofArm.LEFT_HAND_ROLL,
    B1JointIndexWith7DofArm.RIGHT_SHOULDER_PITCH,
    B1JointIndexWith7DofArm.RIGHT_SHOULDER_ROLL,
    B1JointIndexWith7DofArm.RIGHT_ELBOW_PITCH,
    B1JointIndexWith7DofArm.RIGHT_ELBOW_YAW,
    B1JointIndexWith7DofArm.RIGHT_WRIST_PITCH,
    B1JointIndexWith7DofArm.RIGHT_WRIST_YAW,
    B1JointIndexWith7DofArm.RIGHT_HAND_ROLL,
]
