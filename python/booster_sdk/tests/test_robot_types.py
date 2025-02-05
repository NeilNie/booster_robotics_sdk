import unittest
import sys
sys.path.append("../")

from datatypes.robot import (
    GripperMotionParameter,
    ImuState,
    MotorState,
    LowState,
    MotorCmd,
    LowCmd,
    LowCmdType,
)

from booster_robotics_sdk_python import (
    GripperMotionParameter as CppGripperMotionParameter,
    ImuState as CppImuState,
    MotorState as CppMotorState,
    LowState as CppLowState,
    MotorCmd as CppMotorCmd,
    LowCmd as CppLowCmd,
    LowCmdType as CppLowCmdType,
)


class TestGripperMotionParameter(unittest.TestCase):
    def test_init_default(self):
        g = GripperMotionParameter()
        self.assertAlmostEqual(g.position, 0)
        self.assertAlmostEqual(g.force, 0)
        self.assertAlmostEqual(g.speed, 0)

    def test_init_custom(self):
        g = GripperMotionParameter(position=10, force=20, speed=30)
        self.assertAlmostEqual(g.position, 10)
        self.assertAlmostEqual(g.force, 20)
        self.assertAlmostEqual(g.speed, 30)

    def test_from_cpp(self):
        mock_cpp = CppGripperMotionParameter()
        mock_cpp.position = 100
        mock_cpp.force = 200
        mock_cpp.speed = 300

        g = GripperMotionParameter.from_cpp(mock_cpp)
        self.assertAlmostEqual(g.position, 100)
        self.assertAlmostEqual(g.force, 200)
        self.assertAlmostEqual(g.speed, 300)

    def test_to_cpp(self):
        # We can't fully validate the Pybind object without a real module,
        # so we at least check that the fields match.
        g = GripperMotionParameter(position=50, force=60, speed=70)
        cpp_obj = g.to_cpp()
        self.assertAlmostEqual(cpp_obj.position, 50)
        self.assertAlmostEqual(cpp_obj.force, 60)
        self.assertAlmostEqual(cpp_obj.speed, 70)


class TestImuState(unittest.TestCase):
    def test_init(self):
        # ImuState is a placeholder with no fields, so let's just ensure it instantiates
        imu = ImuState()
        self.assertIsInstance(imu, ImuState)

    def test_from_cpp(self):
        mock_cpp = CppImuState()
        imu = ImuState.from_cpp(mock_cpp)
        self.assertIsInstance(imu, ImuState)

    def test_to_cpp(self):
        imu = ImuState()
        cpp_obj = imu.to_cpp()
        # Just ensure we get *some* C++ object back
        self.assertIsNotNone(cpp_obj)


class TestMotorState(unittest.TestCase):
    def test_init_defaults(self):
        ms = MotorState()
        # self.assertAlmostEqual(ms.mode, 0)
        self.assertAlmostEqual(ms.q, 0.0)
        self.assertAlmostEqual(ms.dq, 0.0)
        self.assertAlmostEqual(ms.ddq, 0.0)
        self.assertAlmostEqual(ms.tau_est, 0.0)
        self.assertAlmostEqual(ms.temperature, 0)
        self.assertAlmostEqual(ms.lost, 0)

    def test_init_custom(self):
        ms = MotorState(q=2.0, dq=3.0, ddq=4.0, tau_est=5.0, temperature=6, lost=7)
        # self.assertAlmostEqual(ms.mode, 1)
        self.assertAlmostEqual(ms.q, 2.0)
        self.assertAlmostEqual(ms.dq, 3.0)
        self.assertAlmostEqual(ms.ddq, 4.0)
        self.assertAlmostEqual(ms.tau_est, 5.0)
        self.assertAlmostEqual(ms.temperature, 6)
        self.assertAlmostEqual(ms.lost, 7)

    def test_from_cpp(self):
        mock_cpp = CppMotorState()
        # mock_cpp.mode = 99
        mock_cpp.q = 0.1
        mock_cpp.dq = 0.2
        mock_cpp.ddq = 0.3
        mock_cpp.tau_est = 0.4
        mock_cpp.temperature = 10
        mock_cpp.lost = 11

        ms = MotorState.from_cpp(mock_cpp)
        self.assertAlmostEqual(ms.mode, 99)
        self.assertAlmostEqual(ms.q, 0.1)
        self.assertAlmostEqual(ms.dq, 0.2)
        self.assertAlmostEqual(ms.ddq, 0.3)
        self.assertAlmostEqual(ms.tau_est, 0.4)
        self.assertAlmostEqual(ms.temperature, 10)
        self.assertAlmostEqual(ms.lost, 11)

    def test_to_cpp(self):
        ms = MotorState(q=1.1, dq=2.2, ddq=3.3, tau_est=4.4, temperature=5, lost=6)
        cpp_obj = ms.to_cpp()
        # self.assertAlmostEqual(cpp_obj.mode, 8)
        self.assertAlmostEqual(cpp_obj.q, 1.1)
        self.assertAlmostEqual(cpp_obj.dq, 2.2)
        self.assertAlmostEqual(cpp_obj.ddq, 3.3)
        self.assertAlmostEqual(cpp_obj.tau_est, 4.4)
        self.assertAlmostEqual(cpp_obj.temperature, 5)
        self.assertAlmostEqual(cpp_obj.lost, 6)

    def test_eq(self):
        ms1 = MotorState(q=2.0, dq=3.0)
        ms2 = MotorState(q=2.0, dq=3.0)
        ms3 = MotorState(q=2.0, dq=3.0)

        self.assertTrue(ms1 == ms2)
        self.assertFalse(ms1 == ms3)


# class TestLowState(unittest.TestCase):
#     def test_init_defaults(self):
#         ls = LowState()
#         self.assertIsInstance(ls.imu_state, ImuState)
#         self.assertAlmostEqual(ls.motor_state_parallel, [])
#         self.assertAlmostEqual(ls.motor_state_serial, [])

#     def test_init_custom(self):
#         ms1 = MotorState(mode=1)
#         ms2 = MotorState(mode=2)
#         ls = LowState(imu_state=ImuState(),
#                       motor_state_parallel=[ms1],
#                       motor_state_serial=[ms2])
#         self.assertAlmostEqual(len(ls.motor_state_parallel), 1)
#         self.assertAlmostEqual(len(ls.motor_state_serial), 1)
#         self.assertAlmostEqual(ls.motor_state_parallel[0].mode, 1)
#         self.assertAlmostEqual(ls.motor_state_serial[0].mode, 2)

#     def test_from_cpp(self):
#         # We'll mock the C++ LowState object, along with its .imu_state, .motor_state_parallel, and .motor_state_serial
#         mock_cpp = MagicMock()
#         mock_cpp.imu_state = MagicMock()
#         mock_cpp.motor_state_parallel = [MagicMock(mode=10), MagicMock(mode=20)]
#         mock_cpp.motor_state_serial = [MagicMock(mode=30)]

#         ls = LowState.from_cpp(mock_cpp)
#         self.assertAlmostEqual(len(ls.motor_state_parallel), 2)
#         self.assertAlmostEqual(ls.motor_state_parallel[0].mode, 10)
#         self.assertAlmostEqual(ls.motor_state_parallel[1].mode, 20)
#         self.assertAlmostEqual(len(ls.motor_state_serial), 1)
#         self.assertAlmostEqual(ls.motor_state_serial[0].mode, 30)

#     def test_to_cpp(self):
#         ms1 = MotorState(mode=5)
#         ms2 = MotorState(mode=6)
#         ls = LowState(
#             imu_state=ImuState(),
#             motor_state_parallel=[ms1],
#             motor_state_serial=[ms2]
#         )
#         cpp_obj = ls.to_cpp()
#         # The result is a CppLowState, which has .imu_state and two vectors of MotorState
#         self.assertAlmostEqual(len(cpp_obj.motor_state_parallel), 1)
#         self.assertAlmostEqual(cpp_obj.motor_state_parallel[0].mode, 5)
#         self.assertAlmostEqual(len(cpp_obj.motor_state_serial), 1)
#         self.assertAlmostEqual(cpp_obj.motor_state_serial[0].mode, 6)

#     def test_eq(self):
#         ls1 = LowState(motor_state_parallel=[MotorState(mode=1)],
#                        motor_state_serial=[MotorState(mode=2)])
#         ls2 = LowState(motor_state_parallel=[MotorState(mode=1)],
#                        motor_state_serial=[MotorState(mode=2)])
#         ls3 = LowState(motor_state_parallel=[MotorState(mode=9)],
#                        motor_state_serial=[MotorState(mode=2)])

#         self.assertTrue(ls1 == ls2)
#         self.assertFalse(ls1 == ls3)


class TestMotorCmd(unittest.TestCase):
    def test_init_defaults(self):
        mc = MotorCmd()
        self.assertAlmostEqual(mc.mode, 0)
        self.assertAlmostEqual(mc.q, 0.0)
        self.assertAlmostEqual(mc.dq, 0.0)
        self.assertAlmostEqual(mc.tau, 0.0)
        self.assertAlmostEqual(mc.kp, 0.0)
        self.assertAlmostEqual(mc.kd, 0.0)
        self.assertAlmostEqual(mc.weight, 0.0)

    def test_init_custom(self):
        mc = MotorCmd(mode=1, q=0.1, dq=0.2, tau=0.3, kp=0.4, kd=0.5, weight=0.6)
        self.assertAlmostEqual(mc.mode, 1)
        self.assertAlmostEqual(mc.q, 0.1)
        self.assertAlmostEqual(mc.dq, 0.2)
        self.assertAlmostEqual(mc.tau, 0.3)
        self.assertAlmostEqual(mc.kp, 0.4)
        self.assertAlmostEqual(mc.kd, 0.5)
        self.assertAlmostEqual(mc.weight, 0.6)

    def test_from_cpp(self):
        mock_cpp = CppMotorCmd()
        mock_cpp.mode = 2
        mock_cpp.q = 0.1
        mock_cpp.dq = 0.2
        mock_cpp.tau = 0.3
        mock_cpp.kp = 0.4
        mock_cpp.kd = 0.5
        mock_cpp.weight = 0.6

        mc = MotorCmd.from_cpp(mock_cpp)
        self.assertAlmostEqual(mc.mode, 2)
        self.assertAlmostEqual(mc.q, 0.1)
        self.assertAlmostEqual(mc.dq, 0.2)
        self.assertAlmostEqual(mc.tau, 0.3)
        self.assertAlmostEqual(mc.kp, 0.4)
        self.assertAlmostEqual(mc.kd, 0.5)
        self.assertAlmostEqual(mc.weight, 0.6)

    def test_to_cpp(self):
        mc = MotorCmd(mode=7, q=1.1, dq=2.2, tau=3.3, kp=4.0, kd=5.5, weight=6.0)
        cpp_obj = mc.to_cpp()
        self.assertAlmostEqual(cpp_obj.mode, 7)
        self.assertAlmostEqual(cpp_obj.q, 1.1)
        self.assertAlmostEqual(cpp_obj.dq, 2.2)
        self.assertAlmostEqual(cpp_obj.tau, 3.3)
        self.assertAlmostEqual(cpp_obj.kp, 4.0)
        self.assertAlmostEqual(cpp_obj.kd, 5.5)
        self.assertAlmostEqual(cpp_obj.weight, 6.0)

    def test_eq(self):
        mc1 = MotorCmd(mode=1, q=2.0)
        mc2 = MotorCmd(mode=1, q=2.0)
        mc3 = MotorCmd(mode=3, q=2.0)

        self.assertTrue(mc1 == mc2)
        self.assertFalse(mc1 == mc3)


class TestLowCmd(unittest.TestCase):
    def test_init(self):
        # Suppose we have 4 joints, and a known LowCmdType
        cmd = LowCmd(num_joints=4, cmd_type=LowCmdType.PARALLEL)
        self.assertAlmostEqual(cmd.cmd_type, LowCmdType.PARALLEL)
        self.assertAlmostEqual(len(cmd.motor_cmd), 4)
        for mc in cmd.motor_cmd:
            self.assertIsInstance(mc, MotorCmd)

    def test_to_cpp(self):
        # We'll do a minimal test that ensures we can set some fields and convert to a C++ object
        cmd = LowCmd(num_joints=2, cmd_type=LowCmdType.PARALLEL)
        cmd.motor_cmd[0].q = 1.0
        cmd.motor_cmd[1].q = 2.0

        cpp_obj = cmd.to_cpp()
        # Check that the top-level field matches
        self.assertAlmostEqual(cpp_obj.cmd_type, LowCmdType.PARALLEL.value)
        # Check motor cmds
        self.assertAlmostEqual(len(cpp_obj.motor_cmd), 2)
        self.assertAlmostEqual(cpp_obj.motor_cmd[0].q, 1.0)
        self.assertAlmostEqual(cpp_obj.motor_cmd[1].q, 2.0)


if __name__ == '__main__':
    unittest.main()
