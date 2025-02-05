from booster_robotics_sdk_python import B1LowCmdPublisher as CppB1LowCmdPublisher
from datatypes.robot import LowCmd


class B1LowCmdPublisher:
    """
    A Pythonic wrapper around the C++ pybind B1LowCmdPublisher.

    Provides methods:
        - init_channel()
        - write(low_cmd)
        - close_channel()
        - get_channel_name()

    which correspond to the underlying C++ functionality.

    Example Usage:
        from b1_low_cmd_publisher import B1LowCmdPublisher
        from wrapper import LowCmd
        import time

        pub = B1LowCmdPublisher()
        pub.init_channel()

        while True:
            cmd = LowCmd(...)  # fill in fields
            pub.write(cmd)
            print(\"Published a LowCmd!\")
            time.sleep(1)
    """

    def __init__(self):
        # Create an instance of the raw C++ B1LowCmdPublisher
        self._cpp_pub = CppB1LowCmdPublisher()

    def init_channel(self) -> None:
        """
        Initialize the publication channel (C++ side).
        After calling this, you can start calling write() to publish messages.
        """
        self._cpp_pub.InitChannel()

    def write(self, low_cmd: LowCmd) -> bool:
        """
        Publish a low-level command message via the C++ publisher.
        
        :param low_cmd: A Pythonic LowCmd object that will be converted to the raw C++ LowCmd.
        :return: Boolean indicating success/failure from the underlying C++ call.
        """
        # Convert the Python LowCmd to the raw C++ LowCmd, then call the C++ publisher's Write().
        cpp_obj = low_cmd.to_cpp()
        return self._cpp_pub.Write(cpp_obj)

    def close_channel(self) -> None:
        """
        Close the publication channel in C++, stopping any future publish calls.
        """
        self._cpp_pub.CloseChannel()

    def get_channel_name(self) -> str:
        """
        Return the name of the low cmd publication channel used by this publisher.
        """
        return self._cpp_pub.GetChannelName()
