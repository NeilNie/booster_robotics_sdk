from booster_robotics_sdk_python import B1LowStateSubscriber as CppB1LowStateSubscriber
from datatypes.robot import LowState


class B1LowStateSubscriber:
    """
    A Pythonic wrapper around the C++ pybind B1LowStateSubscriber.

    Example usage:
        def my_handler(low_state: LowState):
            # Do something with the Pythonic LowState
            print(f\"Motor count: {len(low_state.motor_state_serial)}\")

        subscriber = B1LowStateSubscriber(my_handler)
        subscriber.init_channel()
        ...
        subscriber.close_channel()

    Internally, this class:
      - Creates a C++ B1LowStateSubscriber, passing a callback that
        converts the raw C++ LowState to a Python LowState.
      - Exposes the same methods as the C++ class: InitChannel, CloseChannel, etc.
    """

    def __init__(self, user_handler):
        """
        :param user_handler: A Python function that accepts a single parameter (a Python LowState).
        """
        # We'll define an internal callback to pass to the C++ subscriber.
        # This callback receives a C++ LowState, converts it, then calls the user handler.
        def _internal_cpp_callback(cpp_low_state):
            # Convert the raw C++ object to your Pythonic LowState
            py_low_state = LowState.from_cpp(cpp_low_state)
            # Call the user-provided handler with the Pythonic LowState
            user_handler(py_low_state)

        self._cpp_subscriber = CppB1LowStateSubscriber(_internal_cpp_callback)

    def init_channel(self) -> None:
        """
        Initialize the subscription channel in C++.
        After calling this, the callback will begin to receive messages.
        """
        self._cpp_subscriber.InitChannel()

    def close_channel(self) -> None:
        """
        Close the subscription channel in C++ to stop receiving messages.
        """
        self._cpp_subscriber.CloseChannel()

    def get_channel_name(self) -> str:
        """
        Returns the channel name used by this subscriber.
        """
        return self._cpp_subscriber.GetChannelName()
