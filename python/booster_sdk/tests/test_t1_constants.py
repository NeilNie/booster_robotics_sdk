import unittest
import sys
sys.path.append("../")

from constants.t1 import (
    RobotMode,
    B1JointIndex,
    B1JointIndexWith7DofArm,
    B1LocoApiId,
    B1HandAction,
    B1HandIndex,
    GripperControlMode,
    Frame,
    B1_JOINT_CNT_7_DOF_ARM,
    B1_JOINT_CNT,
    B1_JOINTS_7_DOF_ARM
)


class TestEnums(unittest.TestCase):
    def test_RobotMode(self):
        for mode in RobotMode:
            # Accessing each enum member should not raise an exception
            self.assertIsNotNone(mode.value)

    def test_B1JointIndex(self):
        for idx in B1JointIndex:
            self.assertIsNotNone(idx.value)

    def test_B1JointIndexWith7DofArm(self):
        for idx in B1JointIndexWith7DofArm:
            self.assertIsNotNone(idx.value)

    def test_B1LocoApiId(self):
        for api_id in B1LocoApiId:
            self.assertIsNotNone(api_id.value)

    def test_B1HandAction(self):
        for action in B1HandAction:
            self.assertIsNotNone(action.value)

    def test_B1HandIndex(self):
        for hand_idx in B1HandIndex:
            self.assertIsNotNone(hand_idx.value)

    def test_GripperControlMode(self):
        for mode in GripperControlMode:
            self.assertIsNotNone(mode.value)

    def test_Frame(self):
        for frm in Frame:
            self.assertIsNotNone(frm.value)

    def test_B1JointCntConstants(self):
        # Access the constants to ensure no exception occurs
        self.assertIsNotNone(B1_JOINT_CNT_7_DOF_ARM)
        self.assertIsNotNone(B1_JOINT_CNT)
        self.assertIsNotNone(B1_JOINTS_7_DOF_ARM)


if __name__ == "__main__":
    unittest.main()
